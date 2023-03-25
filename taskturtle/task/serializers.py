from rest_framework import serializers
from .models import TaskData, Boards, TaskList


class TaskDataSerialzer(serializers.ModelSerializer):

    class Meta:
        model = TaskData
        fields = ["id", "title", "description", "members", "created_by", "created_at", "updated_at"]


class TaskListSerialzier(serializers.ModelSerializer):

    class Meta:
        model = TaskList
        fields = ["name", "board"]


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boards
        fields = ["id", "title", "image", "created_by", "allowed_to", "created_at", "updated_at"]


    def create(self, validated_data):
        task_list_names = ["Todo", "InProgress", "Done"]
        board = Boards.objects.create(**validated_data)
        for name in task_list_names:
            TaskList.objects.create(board=board, name=name)
        return board

