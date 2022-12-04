from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class table():


class Customer():

