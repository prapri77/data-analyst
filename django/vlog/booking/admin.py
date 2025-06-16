from django.contrib import admin
from .models import bus, Flight, Train, Booking
from django.urls import path
from django.http import HttpResponse

# Register your models here.

class busAdmin(admin.ModelAdmin):
    # listiong the details as table in admin
    list_display = (
        "name",
        "bus_number",
        "bus_type",
        "seat_type",
        "source",
        "destination",
        "price",
    )

    # enable the link to open the record
    list_display_links = ("bus_number", "seat_type")
    # adding the edit option for this that column must not display_links like above
    list_editable = ("name", "price", "source", "destination")
    list_per_page = 6
    # defining search columns
    # search_fields = ("name", "price", "source", "destination")
    search_fields = ("price__gte",)
    list_filter = ("source", "destination")
    ordering = ("price", "name")


class TrainAdmin(admin.ModelAdmin):
    # listiong the details as table in admin
    list_display = (
        "engine_number",
        "name",
        "train_type",
        "seat_type",
        "source",
        "destination",
        "price",
    )

    list_per_page = 6
    readonly_fields = (
        "engine_number",
        "train_type",
        "seat_type",
        "source",
        "destination",
    )

    fieldsets = (
        "Customizable fields",
        {"fields": ("name", "arrival_time", "departure_time", "price")},
    ), (
        "important details",
        {
            "fields": (
                "engine_number",
                "train_type",
                "seat_type",
                "source",
                "destination",
            )
        },
    )





#user defined ui for flights we do admin panel configurations

class FlightAdmin(admin.ModelAdmin):
    change_list_template = "flights.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("custom-view/", self.admin_site.admin_view(self.custom_view))
        ]
        return custom_urls + urls

    def custom_view(self, request):
        return HttpResponse("different page admin view")
    

admin.site.register(bus, busAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Flight)  # , FlightAdmin)

