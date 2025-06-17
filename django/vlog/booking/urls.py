from django.urls import path,include
from .views import ( busdetail,bus_ud,
                    Train_ud,TrainCrud,
                    bulk_create_bus,bulk_create_trains,
                    flight_ui,bus_html,
                    train_html,select_bus,
                    select_train,booking_view,
                    booking_html_data,BookingViewSet,
                    BusViewSet,TrainViewSet,
                    FlightViewSet)


from rest_framework.routers import DefaultRouter
from django.urls import include
#create a router and register the bookingviewset with it
router = DefaultRouter()
# Register the serializers with the router
router.register(r'bookview', BookingViewSet, basename='bookview')
router.register(r'busview', BusViewSet, basename='busview')
router.register(r'trainview', TrainViewSet, basename='trainview')
router.register(r'flightview', FlightViewSet, basename='flightview')

app_name = "vlog"


urlpatterns = [
    path("bus", busdetail, name= "bus"),
    path("bus_ud/<int:id>", bus_ud),
    path("train", TrainCrud.as_view()),
    path("train_ud/<int:id>",Train_ud),
    path("bulk_create", bulk_create_bus),
    path("bulk_create_t", bulk_create_trains),
    path("flight",flight_ui),
    path("flights/", flight_ui, name="flight_data_view"),
    path("buses", bus_html, name="buses"),
    path("trains", train_html, name= "trains"),
    path("sel_bus/<int:id>",select_bus, name="sel_bus"),
    path("sel_train/<int:id>", select_train, name="sel_train"),
    path("booking", booking_view, name="booking"),
    path("book_html/<str:data>", booking_html_data, name="book_html"), #here we should type id and transport type to see booking confirmed or not
    path("",include(router.urls)),
]
