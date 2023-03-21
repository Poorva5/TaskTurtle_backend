from rest_framework import serializers
from .models import TaskData, Boards


class TaskDataSerialzer(serializers.ModelSerializer):

    class Meta:
        model = TaskData
        fields = ["id", "title", "description", "status", "members", "board", "created_by", "created_at", "updated_at"]

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boards
        fields = ["id", "title", "image", "created_by", "allowed_to", "created_at", "updated_at"]

