from django.urls import path,include
from .views import busdetail,bus_ud,Train_ud,TrainCrud,bulk_create_bus,bulk_create_trains,flight_ui



urlpatterns = [
    path("bus", busdetail),
    path("bus_ud/<int:id>", bus_ud),
    path("train", TrainCrud.as_view()),
    path("train_ud/<int:id>",Train_ud),
    path("bulk_create", bulk_create_bus),
    path("bulk_create_t", bulk_create_trains),
    path("flight",flight_ui),
    path("flights/", flight_ui, name="flight_data_view"),
]
