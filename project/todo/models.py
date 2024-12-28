from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  task_name = models.CharField(max_length=100)
  finished = models.BooleanField(default=False)

  def __str__(self):
    return self.task_name