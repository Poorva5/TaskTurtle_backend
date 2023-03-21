from django.db import models
from taskturtle.utils.models import BaseModel
from taskturtle.users.models import User

class Boards(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='boards_image', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    allowed_to = models.ManyToManyField(User)


    def __srt__(self):
        return self.title


class TaskData(BaseModel):

    class StatusChoices(models.TextChoices):
        TODO = 'Todo'
        BACKLOGS = 'Backlogs'
        IN_PROGRESS = 'In Progress'
        IN_REVIEW = 'In Review'
        TESTING = 'Testing'
        DONE = 'Done'
        COMPLETED = 'Completed'

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=StatusChoices.choices, max_length=255, default=StatusChoices.TODO)
    members = models.ManyToManyField(User, related_name='members')
    board = models.ForeignKey(Boards, on_delete=models.CASCADE, related_name='board')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)




