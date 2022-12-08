from django.db import models
from datetime import date, timedelta 


class Reservation(models.Model):
    name = models.CharField(max_length=100, default="Placeholder")
    number_of_persons = models.IntegerField()
    email = models.CharField(max_length=150, default="Placeholder")
#    date = models.DateField()
#    time = models.TimeField()
#    booking_date_time_start = models.DateTimeField()
#    booking_date_time_end = models.DateTimeField()

    def __str__(self):
        return self.name
        


# class Table(models.Model):
#   table = models.ForeignKey(Table)
#   size = models.IntegerField()


# class Customer():
#    name = models.CharField(max_length=100)
#    email = models.EmailField(max_length=150)
#    phone = models.IntegerField()
#    number_of_persons = models.IntegerField()
