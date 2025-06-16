from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import bus,Train,Flight,Booking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import FlightForm

# Create your views here.
@csrf_exempt
def busdetail(request):
    if request.method == "POST":
       payload = json.loads(request.body)

       #creating  bus record using the passes json payloads
       instance = bus.objects.create(
           bus_number = payload.get("bus_number"),
           name = payload.get("name"),
           bus_type = payload.get("bus_type"),
           seat_type = payload.get("seat_type"),
           source = payload.get("source"),
           destination = payload.get("destination"),
           arrival_time = payload.get("arrival_time"),
           departure_time = payload.get("departure_time"),
           price = payload.get("price"),
       )
       return JsonResponse(
           {
               "message": "record created", 
            "details":{
                "id":instance.id,
                "name":instance.name,
                "bus_number":instance.bus_number
                }
            }
       )
    #after creating we getting all datas
    elif request.method == "GET":
        records = bus.objects.all()
        buses_list = []
        for record in records:
            buses_list.append(
                {
                    "vehicle_number": record.bus_number,
                    "travels_name": record.name,
                    "boarding_point": record.source,
                    "destined_locations": record.destination,
                    "boarding_time": record.arrival_time,
                    "bus_type": record.bus_type,
                    "seat_type": record.seat_type

                }
            )
        
        return JsonResponse(buses_list, safe=False)

@csrf_exempt
def bus_ud(request, id):
    """
    this function received the record id to update or deleted the record
    """
    if request.method == "PUT": 
        payload = json.loads(request.body)
        # filtering the specific record
        # instance = Bus.objects.filter()
        instance = bus.objects.get(id=id)

        instance.bus_number = payload.get("bus_number", instance.bus_number)
        instance.name = payload.get("name", instance.name)
        instance.bus_type = payload.get("bus_type", instance.bus_type)
        instance.seat_type = payload.get("seat_type", instance.seat_type)
        instance.source = payload.get("source", instance.source)
        instance.destination = payload.get("destination", instance.destination)
        instance.arrival_time = payload.get("arrival_time", str(instance.arrival_time))
        instance.departure_time = payload.get("departure_time", str(instance.departure_time))
        instance.price = payload.get("price", instance.price)
        instance.save()

        return JsonResponse(
            {
                "message": "record updated",
                "details": {
                    "id": instance.id,
                    "name": instance.name,
                    "bus_number": instance.bus_number,
                },
            }
        )
    elif request.method == "DELETE":
        instance = bus.objects.get(id=id)
        instance.delete()
        return JsonResponse({"message": "record delete"})


#create view for train crud
class TrainCrud(APIView):
    def get(self, request):
        data = Train.objects.all().values()
        return Response(data)

    def post(self, request):
        payload = request.data
        Train.objects.create(
            engine_number=payload.get("engine_number"),
            name=payload.get("name"),
            train_type=payload.get("train_type"),
            seat_type=payload.get("seat_type"),
            source=payload.get("source"),
            destination=payload.get("destination"),
            arrival_time=payload.get("arrival_time"),
            departure_time=payload.get("departure_time"),
            price=payload.get("price"),
        )
        return Response("Train record created successfully")


@api_view(["PUT", "DELETE"])
def Train_ud(request, id):

    if request.method == "PUT":
        payload = request.data
        instance = Train.objects.get(id=id)
        instance.engine_number = payload.get("engine_number", instance.engine_number)
        instance.name = payload.get("name", instance.name)
        instance.train_type = payload.get("train_type", instance.train_type)
        instance.seat_type = payload.get("seat_type", instance.seat_type)
        instance.source = payload.get("source", instance.source)
        instance.destination = payload.get("distination", instance.destination)
        instance.arrival_time = payload.get("arrival_time", instance.arrival_time)
        instance.departure_time = payload.get("departure_time", instance.departure_time)
        instance.price = payload.get("price", instance.price)
        instance.save()

        return Response("record updated")
    elif request.method == "DELETE":
        instance = Train.objects.get(id=id)
        instance.delete()
        return Response("record deleted")


@api_view(["GET", "POST"])
def bulk_create_bus(request):
    if request.method == "POST":

        data = request.data

        # bulk create will save time
        Buses = [
            bus(
                bus_number=payload.get("bus_number"),
                name=payload.get("name"),
                bus_type=payload.get("bus_type"),
                seat_type=payload.get("seat_type"),
                source=payload.get("source"),
                destination=payload.get("destination"),
                arrival_time=payload.get("arrival_time"),
                departure_time=payload.get("departure_time"),
                price=payload.get("price"),
            )
            for payload in data
        ]

        bus.objects.bulk_create(Buses)
        return Response("Bulk creation of bussess successfuly")
    else:
        return Response("pass massive data to process and store in db")
    
@api_view(["GET", "POST"])
def bulk_create_trains(request):
    if request.method == "POST":

        data = request.data

        # bulk create will save time
        Trains = [
            Train(
                engine_number=payload.get("engine_number"),
                name=payload.get("name"),
                train_type=payload.get("train_type"),
                seat_type=payload.get("seat_type"),
                source=payload.get("source"),
                destination=payload.get("destination"),
                arrival_time=payload.get("arrival_time"),
                departure_time=payload.get("departure_time"),
                price=payload.get("price"),
            )
            for payload in data
        ]

        Train.objects.bulk_create(Trains)
        return Response("Bulk creation of trains successfuly")
    else:
        return Response("pass massive data to process and store in db")

def flight_ui(request):
    if request.method == "POST":
        # validating the HTML data
        form = FlightForm(request.POST)
        print("received form ", form)
        if form.is_valid():
            form.save()
            return HttpResponse("Flight Data processed successfully")
    else:
        flights = Flight.objects.all().order_by("-departure_time")
        form = FlightForm()
        context = {"form": form, "flights": flights}

    return render(request, "flights_data.html", context)
