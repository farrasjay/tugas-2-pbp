from django.db import models
from django.contrib.auth.models import User

class toDoList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    creation_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    is_finished = models.BooleanField(default = False)