from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import User_Serializer, Group_Serializers
from django.http import HttpResponse


class User_Viewset( viewsets.ModelViewSet ):
    '''
    API endpoint that allows users to be viewed or edited
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = User_Serializer

class Group_Viewset( viewsets.ModelViewSet ):
    '''
    API endpoint that allows groups to be viewed or edited
    '''
    queryset = Group.objects.all()
    serializer_class = Group_Serializers
