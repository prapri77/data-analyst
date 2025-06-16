from django.db import models
from accounts.models import User

# Create your BUS models here.
class bus(models.Model):
    BUS_TYPE = [("AC", "airconditioned prime bus"),("Non Ac", "normal bus")]
    SEAT_TYPE = [("SL", "sleeper"),("SE","seater")]

    bus_number = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    bus_type = models.CharField(max_length=100,choices=BUS_TYPE, blank=True,null=True)
    seat_type = models.CharField(max_length=100,choices=SEAT_TYPE, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True,null=True)
    destination = models.CharField(max_length=100,blank=True,null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "vlog"
    
     

# Create your Train models here.
class Train(models.Model):
    TRAIN_TYPE = [("1st tier", "AC"),("2nd tier", "AIR C"),("Non ac","normal train")]
    SEAT_TYPE = [
        ("SL","SLEEPER"),
        ("G","GENERAL"),
        ("SC","SECONDCLASS"),
        ("FC","FIRSTCLASS")
    ]

    engine_number = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    train_type = models.CharField(max_length=100,choices=TRAIN_TYPE,blank=True,null=True)
    seat_type = models.CharField(max_length=100,choices=SEAT_TYPE,blank=True,null=True)
    source = models.CharField(max_length=100,blank=True,null=True)
    destination = models.CharField(max_length=100,blank=True,null=True)
    arrival_time = models.DateTimeField(blank=True,null=True)
    departure_time = models.DateTimeField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name
    
#create models for flights here
class Flight(models.Model):
    CLASS_TYPE = [
        ("E","ECONOMIC"),
        ("B","BUSINESS")
    ]

    flight_number = models.CharField(max_length=100,blank=True,null=True)
    airline = models.CharField(max_length=100,blank=True,null=True)
    class_type = models.CharField(max_length=100,choices=CLASS_TYPE,blank=True,null=True)
    source = models.CharField(max_length=100,blank=True,null=True)
    destination = models.CharField(max_length=100, blank=True,null=True)
    arrival_time = models.DateTimeField(blank=True,null=True)
    departure_time = models.DateTimeField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.airline
    
#create models for booking here
class Booking(models.Model):
    TRANSPORT_CHOICES = [
        ("Bus","Bus"),
        ("Train","Train"),
        ("Flight","Flight"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport_type = models.CharField(max_length=100,choices=TRANSPORT_CHOICES,blank=True,null=True)
    transport_id = models.PositiveBigIntegerField() #will store id of bus/flight/train
    travel_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="confirmed")

    def __str__(self):
        return self.user.full_name