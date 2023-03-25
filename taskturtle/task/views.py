from django.shortcuts import render
from rest_framework import viewsets
from .models import TaskData, Boards, TaskList
from .serializers import TaskDataSerialzer, BoardSerializer, TaskListSerialzier


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskData.objects.all()
    serializer_class = TaskDataSerialzer
    

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerialzier

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        return TaskList.objects.filter(board_id=board_id)
        
