from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Booking,bus,Train,Flight

class BookingSerializer(ModelSerializer):
    travel_details = SerializerMethodField()

    def get_travel_details(self, obj):
        if obj.transport_type == 'bus':
            bus= bus.objects.get(id=obj.transport_id)
            return {
                'name': bus.name,
                'source': bus.source,
                'destination': bus.destination,
                'departure_time': bus.departure_time,
                'arrival_time': bus.arrival_time,
                'price': bus.price,
            }
        elif obj.transport_type == 'train':
            train = Train.objects.get(id=obj.transport_id)
            return {
                'name': train.name,
                'source': train.source,
                'destination': train.destination,
                'departure_time': train.departure_time,
                'arrival_time': train.arrival_time,
                'price': train.price,
            }
        elif obj.transport_type == 'flight':
            try:
                flight = Flight.objects.get(id=obj.transport_id)
                return {
                    'airline': flight.airline,
                    'source': flight.source,
                    'destination': flight.destination,
                    'departure_time': flight.departure_time,
                    'arrival_time': flight.arrival_time,
                    'price': flight.price,
                }
            except Flight.DoesNotExist:
                # Handle the case where the flight does not exist
                return {
                    'error': 'Flight not found'
                }
        

    class Meta:
        model = Booking
        fields = '__all__'

class BusSerializer(ModelSerializer):
    class Meta:
        model = bus
        fields = '__all__'

class TrainSerializer(ModelSerializer): 
    class Meta:
        model = Train
        fields = '__all__'

class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'