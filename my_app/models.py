from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()


class Car(models.Model):
    brand = models.CharField(max_length=20)
    year = models.IntegerField()


    def __str__(self):
        return f"Car brand is {self.brand} {self.year} "
    