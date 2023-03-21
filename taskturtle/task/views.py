from django.shortcuts import render
from rest_framework import viewsets
from .models import TaskData, Boards
from .serializers import TaskDataSerialzer, BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskData.objects.all()
    serializer_class = TaskDataSerialzer
    


