from django.contrib import admin
from .models import Boards, TaskData, TaskList

@admin.register(Boards)
class BoardAdmin(admin.ModelAdmin):
    list_display = ["title", "created_by"]

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ["name", "board"]

@admin.register(TaskData)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_by"]
