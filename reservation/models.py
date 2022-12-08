from django.db import models
from . import forms
from django import date, timedelta 


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    start_month = models.DateField()
    end_month = models.DateField()
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self) -> str:
        return str(self.name)


# class Reservation(models.Model):
#    name = models.CharField(max_length=100)
#    number_of_persons = models.IntegerField()
#    date = models.DateField()
#    time = models.TimeField()
#    booking_date_time_start = models.DateTimeField()
#    booking_date_time_end = models.DateTimeField()

#    def __str__(self):
#        return self.name
        



# class Table(models.Model):
#   table = models.ForeignKey(Table)
#   size = models.IntegerField()


# class Customer():
#    name = models.CharField(max_length=100)
#    email = models.EmailField(max_length=150)
#    phone = models.IntegerField()
#    number_of_persons = models.IntegerField()
