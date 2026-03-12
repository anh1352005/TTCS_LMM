from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User
from  .serializers import RegisterSerializer,UserSerializer
# Create your views here.
#Dung viewset voi crud con api voi logic dac biet
class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
#tao token de register + login luon
class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user).data,
                "token":token.key
            })
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(username=username,password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token":token.key
            })
        return self.response({"error":"Invalid"},status=status.HTTP_400_BAD_REQUEST)




