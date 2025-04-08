from django.db import models

# Create your models here.

class FarmReport(models.Model):
    areasize = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quality = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    phone = models.CharField(max_length=20)
    farmtype = models.CharField(max_length=100)
    image = models.ImageField(upload_to='farm_images/')

    def __str__(self):
        return f"{self.farmtype} - {self.location}"
