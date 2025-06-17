from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import permission_classes, authentication_classes

# Create your views here.


def home_page(request):
    return render(request, 'home.html')

@authentication_classes([])
@permission_classes([])
def signup_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        full_name = request.POST["full_name"]
        password = request.POST["password"]

        #check wheather if exists email or not
        if User.objects.filter(email=email).exists():
            messages.error("this email already exists")
        else:
            user = User.objects.create(
                email = email,
                phone_number = phone_number,
                full_name = full_name,
                password = password,
            )
            return redirect("home")
        
    return render(request, "signup.html")

@authentication_classes([])
@permission_classes([])
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            messages.error(request, "wrong credentials")

    
    return render(request, "login.html")

@csrf_exempt
def main_page(request):
    return render(request, "main.html", {"email":request.user.email, "full_name":request.user.full_name},)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])  
def token_view(request): #generate token for user
    """
    Generate a token for the user if they are authenticated.
    sample json request body:
    {
        "email": " 
        "password": "your_password"
    }
    """
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
       
       