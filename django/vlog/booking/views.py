from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import bus,Train,Flight,Booking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from .forms import FlightForm,busForm,TrainForm, BookingForm
from django.contrib import messages
from datetime import date
from .serializers import BookingSerializer, BusSerializer, TrainSerializer, FlightSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
@csrf_exempt
def busdetail(request): # this need postman to insert record for developers
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
def bus_ud(request, id): #this also need postman
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


def bus_html(request):
    """
    handles GET and POST request to list buses and create new bus record
    """
    form = busForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,"bus record created successfully.")
            return redirect("bus_html") #replace with your url name
        else:
            messages.error(request, "Invalid bus data submitted.")
    
    bus_data = bus.objects.all().order_by("-id")
    return render(request, "bus.html", {"form": form, "buses":bus_data})

def train_html(request):
    """
    handles GET and POST request to list trains and create new train record
    """
    form = TrainForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,"Train record created successfully.")
            return redirect("Train_html") #replace with your url name
        else:
            messages.error(request, "Invalid Train data submitted.")
    
    train_data = Train.objects.all().order_by("-id")
    return render(request, "train.html", {"form": form, "trains":train_data})

def select_bus(request, id):
    data = get_object_or_404(bus, id=id)
    # data = get_object_or_404(bus, id=id)
    return render(request, "selected_bus.html", 
                  {"bus": data, "booking_details": str(data.id) + ", bus" },
                  )

def select_train(request, id):
    train = get_object_or_404(Train, id=id)
    return render(request, 
                  "selected_train.html", 
                  {"train": train, "booking_details": str(train.id) + ", train"},
                  )


def booking_view(request):
    """
    this method must handle three cases initially from the selected_bus or selected_train html
    we can use post part otherwise we need to send the booking.html to receive data

    """
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = "confirmed"
            form.save()
            messages.success(request, "booking created")
            # return redirect("main")

        else:
            messages.error(request, "invalid datas you passed")

    form = BookingForm()
    # taking the user detaisl and returning all the bookings existing
    existing_bookings = Booking.objects.filter(user=request.user.id).order_by(
        "-booking_date"
    )
    return render(
        request,
        "booking.html",
        {"form": form, "existing_bookings": existing_bookings},
    )


@csrf_exempt
def booking_html_data(request, data):
    print("booking from data htmls ", data)
    record_id, type = data.strip().lower().split(",")

    instance = None
    vehicle = None

    if type.strip() == "bus":
        vehicle = get_object_or_404(bus, id=int(record_id))
        instance = Booking.objects.create(
            user=request.user,
            transport_type="Bus",
            transport_id=vehicle.id,
            travel_date=(
                vehicle.arrival_time.date() if vehicle.arrival_time else date.today()
            ),
        )

    elif type.strip() == "train":
        vehicle = get_object_or_404(Train, id=int(record_id))
        instance = Booking.objects.create(
            user=request.user,
            transport_type="Train",
            transport_id=vehicle.id,
            travel_date=(
                vehicle.arrival_time.date() if vehicle.arrival_time else date.today()
            ),
        )

    elif type.strip() == "flight":
        vehicle = get_object_or_404(Flight, id=int(record_id))
        instance = Booking.objects.create(
            user=request.user,
            transport_type="Flight",
            transport_id=vehicle.id,
            travel_date=(
                vehicle.arrival_time.date() if vehicle.arrival_time else date.today()
            ),
        )

    return render(
        request, "booking_confirmed.html", {"vehicle": vehicle, "booking": instance, "data": data}
    )

class BookingViewSet(ModelViewSet):
    """
    a viewset for viewing and editing  booking instances.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(url_name="my_bookings",detail=False, methods=["get"])
    def my_bookings(self, request):
        """
        the classfiaction of the bookings based on the types of transportation 
        and the user who made the booking.
        """
        user = request.user
        bookings = Booking.objects.filter(user=user).order_by("-booking_date")
        serializer = self.get_serializer(bookings, many=True)
        #classifying bus train flights
        bus_bookings = [b for b in serializer.data if b["transport_type"]== "bus"]
        train_bookings = [b for b in serializer.data if b["transport_type"]== "Train"]
        flights_bookings = [b for b in serializer.data if b["transport_type"]== "Flight"]

        return Response(
            {
                "bus_bookings": bus_bookings,
                "train_bookings": train_bookings,
                "flights_bookings": flights_bookings,
            }
        )

    # def get_queryset(self):
    #     # filter bookings by the logged-in-user
    #     return self.queryset.filter(user=self.request.user)
    
class BusViewSet(ModelViewSet): 
    """
    a viewset for viewing and editing bus instances.
    """

    queryset = bus.objects.all()
    serializer_class = BusSerializer

    def get_queryset(self):
        # filter bookings by the logged-in-user
        return self.queryset.order_by("-id")
    
    @action(url_name="bus_classfication", detail=False, methods=["get"])
    def bus_classfication(self, request):
        """
        this method will classify the buses based on the type of bus
        """
        buses = self.get_queryset()
        bus_types = {"AC": [], "Non Ac": []} 
        #classifying the buses based on the type of bus
        #iterating through the buses and classifying them
        for bus in buses:
            serializer_bus = self.get_serializer(bus).data
            bus_types[bus.bus_type].append(serializer_bus)
        return Response(bus_types)


    # @action(url_name="my_buses", detail=False, methods=["get"])
    # def my_buses(self, request):
    #     user = request.user
    #     buses = bus.objects.filter(user=user).order_by("-id")
    #     serializer = self.get_serializer(buses, many=True)
    #     return Response(serializer.data) 

class TrainViewSet(ModelViewSet):
    """
    a viewset for viewing and editing train instances.
    """

    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_queryset(self):
        # filter bookings by the logged-in-user
        return self.queryset.order_by("-id")
    
    @action(url_name="train_classfication", detail=False, methods=["get"])
    def train_classfication(self, request): 
        """
        this method will classify the trains based on the type of train
        """
        trains = self.get_queryset()
        train_types = {"1st tier": [], "2nd tier": [], "Non ac": []} 
        #classifying the trains based on the type of train
        #iterating through the trains and classifying them
        for train in trains:
            serializer_train = self.get_serializer(train).data
            train_types[train.train_type].append(serializer_train)
        return Response(train_types)    
    

    # @action(url_name="my_trains", detail=False, methods=["get"])
    # def my_trains(self, request):
    #     user = request.user
    #     trains = Train.objects.filter(user=user).order_by("-id")
    #     serializer = self.get_serializer(trains, many=True)
    #     return Response(serializer.data)  

class FlightViewSet(ModelViewSet):
    """
    a viewset for viewing and editing flight instances.
    """

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        # filter bookings by the logged-in-user
        return self.queryset.order_by("-id")

    # @action(url_name="my_flights", detail=False, methods=["get"])
    # def my_flights(self, request):
    #     user = request.user
    #     flights = Flight.objects.filter(user=user).order_by("-id")
    #     serializer = self.get_serializer(flights, many=True)
    #     return Response(serializer.data)         