from django.db import models

# Create your models here.
class TodoData(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    date = models.DateField()