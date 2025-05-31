from django.urls import path,include
from accounts.views import sample_view

urlpatterns = [
    
    path("", sample_view),
]