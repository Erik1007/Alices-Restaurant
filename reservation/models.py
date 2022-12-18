from collections import namedtuple
from datetime import date, timedelta, datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError


class Customer():
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()


TABLE_TIME_CHOICES = [
    ("1", "15:00-17:00",),
    ("2", "16:00-18:00",),
    ("3", "17:00-19:00",),
    ("4", "18:00-20:00",),
    ("5", "19:00-21:00",),
    ("6", "20:00-22:00",),
    ]


class Reservation(models.Model):
    name = models.CharField(max_length=150)
    number_of_persons = models.IntegerField()
    email = models.CharField(max_length=150, null=True)
    date = models.DateField(default=timezone.now)
    tables = models.ManyToManyField(
        'reservation.Table', related_name='reservations')
    booking_time = models.CharField(
        max_length=50, default=1, choices=TABLE_TIME_CHOICES)

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=50, default='placeholder')
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
    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return f'Table {self.id}'


class NewReservation(models.Model):
#    name = models.CharField(max_length=150)
#    available_table = models.ManyToManyField(Reservation)
#    NewReservation = Reservation.objects.create(name='reserved_table')

#    new_reservation.save()

