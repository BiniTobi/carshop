from django.db import models

class Homecars(models.Model):
   
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    model = models.TextField()
    price =models.IntegerField()
    transmition = models.CharField(max_length=150)
    original = models.CharField(max_length=150)
    cc = models.CharField(max_length=150)
    plate = models.CharField(max_length=150)
    condition = models.CharField(max_length=150)

