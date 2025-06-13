from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home_page(request):
    return render(request, 'home.html')

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
       