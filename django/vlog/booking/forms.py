from django.forms import ModelForm
from .models import Flight,Train,bus, Booking
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

class busForm(ModelForm):
    travel_date = forms.DateField(
       widget=forms.DateInput(
          attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Select a travel date",
            }
        ),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = bus
        fields = "__all__"

class TrainForm(ModelForm):
    class Meta:
        model = Train
        fields = "__all__"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # fields = "__all__"
        exclude = ["user", "booking_date", "status"]