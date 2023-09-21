from django.db import models

# Create your models here.
class Service(models.Model):
    sname=models.CharField(max_length=250)
    simg=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.sname