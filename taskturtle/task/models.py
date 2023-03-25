from django.db import models
from taskturtle.utils.models import BaseModel
from taskturtle.users.models import User

class Boards(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='boards_image', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    allowed_to = models.ManyToManyField(User, blank=True, null=True)


    def __srt__(self):
        return self.title


class TaskList(BaseModel):
    name = models.CharField(max_length=255, null=True)
    board = models.ForeignKey(Boards, on_delete=models.CASCADE, related_name='lists', null=True)

    def __str__(self):
        return self.name
        

class TaskData(BaseModel):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='cards', null=True)
    members = models.ManyToManyField(User, related_name='members')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



