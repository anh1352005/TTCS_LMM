from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Seat,SeatReservation,Zone
from .serializers import SeatSerializer,SeatReservationSerializer,ZoneSerializer
# Create your views here.
class ZoneView(viewsets.ModelViewSet):
    queryset=Zone.objects.all()
    serializer_class=ZoneSerializer

class SeatView(viewsets.ModelViewSet):
    queryset=Seat.objects.all()
    serializer_class=SeatSerializer

class SeatReservationView(viewsets.ModelViewSet):
    queryset=SeatReservation.objects.all()
    serializer_class=SeatReservationSerializer

    @action(detail=True,methods=['patch'])
    def check_in(self,request,pk=None):
        reservation=self.get_object()
        reservation.status="occupied"
        reservation.save()
        return Response({"message":"Checked In"})
    
    @action(detail=True,methods=['patch'])
    def check_out(self,request,pk=None):
        reservation=self.get_object()
        reservation.status="finished"
        reservation.save()
        return Response({"message":"Checked Out"})
