from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)