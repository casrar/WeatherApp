from django.db import models

# Create your models here.
class Location(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.CharField(max_length=200, blank=True, null=True)
    country_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name + ', '  + self.state_name + ', ' + self.country_name
