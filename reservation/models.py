from collections import namedtuple
from datetime import date, timedelta, datetime
import pytz
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError


class Table(models.Model):
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return f'Table {self.id}'

    def seat_count(self):
        return self.seats.count()

    def available_seats(self):
        return self.seats.filter(occupied=False).count()


class Seat(models.Model):
    occupied = models.BooleanField(default=False)
    seat = models.ForeignKey(
        'reservation.Table', on_delete=models.SET_NULL, null=True,
        related_name='seats')


class Reservation(models.Model):
    name = models.CharField(max_length=100,)
    number_of_persons = models.IntegerField()
    email = models.CharField(max_length=150, null=True)
    date = models.DateField('Start date', default=datetime.today)
    time = models.TimeField('Start time', timezone.activate(
        pytz.timezone('CET')), default=timezone.now)
    tables = models.ManyToManyField(
        'reservation.Table', related_name='reservations')
#   current_date = datetime.now()
#   bookings = Reservation.objects.filter(date__lt=current_date)
#   bookings.delete()

    def __str__(self):
        return self.name

 
class Customer():
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
