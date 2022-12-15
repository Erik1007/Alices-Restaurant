from collections import namedtuple
from django.contrib.auth.models import User
from datetime import date, timedelta, datetime
import pytz
from django.utils import timezone
from django.db import models
from django import forms
from django.core.exceptions import ValidationError


class TableBooking(models.Model):
    table_number = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('RESERVED', 'Reserved'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='AVAILABLE',
    )
    booking_time = forms.ChoiceField(choices=[
        ("15:00-17:00",),
        ("16:00-18:00",),
        ("17:00-19:00",),
        ("18:00-20:00",),
        ("19:00-21:00",),
        ("20:00-22:00",),
     ])

    def __str__(self):
        return self.table_id


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
    # timeSlots = forms.ChoiceField(
    #    choices=ReservationTime,
    #    widget=forms.ListBox(attrs={"size": len(AVAILABLE_TIMES)})
    # )
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
