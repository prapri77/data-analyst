from account.views import home_page, signup_view, login_view, main_page
from django.urls import path

urlpatterns = [
    path("", home_page, name="home"),
    path("signup", signup_view, name="signup"),
    path("login", login_view, name="login"),
    path("main", main_page, name="main"),
]
