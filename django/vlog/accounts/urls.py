from django.urls import path,include
from accounts.views import home_page,signup_view,login_view,main_page, token_view

urlpatterns = [
    
    path("", home_page, name = "home"),
    path("signup",signup_view, name = "signup"),
    path("login",login_view, name = "login"),
    path("main",main_page, name = "main"),
    path("token", token_view, name="token_view"),
]