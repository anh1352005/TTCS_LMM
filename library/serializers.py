from rest_framework import serializers
from .models import Zone,Seat,SeatReservation

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zone
        field='__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        field='__all__'

class SeatReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=SeatReservation
        field='__all__'
