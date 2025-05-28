from django.db import models
from account.models import User

# Create your models here.
class Bus(models.Model):
    BUS_TYPE = [("AC", "airconditioned prime bus"), ("Non Ac", "normal bus")]
    SEAT_TYPE = [("SL", "sleeper"), ("SE", "seater")]

    bus_number = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    bus_type = models.CharField(max_length=100,choices=BUS_TYPE, blank=True, null=True)
    seat_type = models.CharField(max_length=100,choices=SEAT_TYPE, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    distination = models.CharField(max_length=100, blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Train(models.Model):
    Train_TYPE = [("AC", "airconditioned prime train"), ("Non Ac", "normal train")]
    SEAT_TYPE = [
        ("SL", "sleeper"),
        ("G", "general"),
        ("SC", "secondclass"),
        ("FC", "first class"),
    ]

    engine_number = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    train_type = models.CharField(max_length=100, choices=Train_TYPE blank=True, null=True)
    seat_type = models.CharField(max_length=100,choices=SEAT_TYPE, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    distination = models.CharField(max_length=100, blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


e.
class Flight(models.Model):
    CLASS_TYPE = [
        ("E", "economic"),
        ("B", "business")
    ]

    flight_number = models.CharField(max_length=100, blank=True, null=True)
    airline = models.CharField(max_length=100, blank=True, null=True)
    class_type = models.CharField(max_length=100, choices= CLASS_TYPE,blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    distination = models.CharField(max_length=100, blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    TRANSPORT_CHOICES = [
        ("Bus", "Bus"),
        ("Train", "Train"),
        ("Flight", "Flight"),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES, blank=True, null=True)
    transport_id = models.PositiveBigIntegerField() # will store ID of Bus/Flight/Train
    travel_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="confirmed")

    def __str__(self):
        return self.user.full_name