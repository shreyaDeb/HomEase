from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=4, decimal_places=1)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
