from django.db import models
from django.urls import reverse
 
class Homepage(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    transmition = models.CharField(max_length=150)
    orignal_left_hand_or_not = models.CharField(max_length=150)
    cc = models.CharField(max_length=150)
    plate = models.CharField(max_length=150)
    condition = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    img = models.ImageField(upload_to='pics')

    def get_absolute_url(self):
        return reverse('binicarproject:detail',args=[self.id,])
        
