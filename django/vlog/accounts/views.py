from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from accounts.models import User

# Create your views here.


def sample_view(request):
    return HttpResponse("HELLO PRASANTH")