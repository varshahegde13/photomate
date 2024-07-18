from rest_framework import serializers
from .models import Photographer, Event,Booking

class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

        