from django.forms import ModelForm
from .models import Flight
from django import forms


class FlightForm(ModelForm):
    departure_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), required=False
    )
    arrival_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), required=False
    )

    class Meta:
        model = Flight
        fields = "__all__"
