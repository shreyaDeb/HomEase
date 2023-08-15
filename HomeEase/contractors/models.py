from django.db import models

# Create your models here.

class Contractor(models.Model):
    name = models.CharField(max_length=100)
    services = models.TextField()
    contact_email = models.EmailField()
    phone_country_code = models.IntegerField()  # Country code
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
