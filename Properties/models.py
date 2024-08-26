from django.db import models

# Create your models here.

class Advertise(models.Model):
      property_type = models.CharField(max_length=255)
      number_of_rooms = models.IntegerField()
      location = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.CharField(max_length=500)
      images = models.ImageField(upload_to='property_images/'),
      user = models.ForeignKey('auth.user',on_delete=models.CASCADE)
      sold = models.BooleanField(default=False)
      