from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=50)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
