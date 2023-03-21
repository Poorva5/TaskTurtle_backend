from django.contrib import admin
from .models import Boards, TaskData

@admin.register(Boards)
class BoardAdmin(admin.ModelAdmin):
    list_display = ["title", "created_by"]


@admin.register(TaskData)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "board", "status", "created_by"]
