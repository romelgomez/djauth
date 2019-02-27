from django.shortcuts import render 
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    return HttpResponse('home view')
    

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer