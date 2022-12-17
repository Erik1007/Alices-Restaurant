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


class Reservation(models.Model):
    number_of_persons = models.IntegerField()
    email = models.CharField(max_length=150, null=True)
    date = models.DateField(default=timezone.now)
    tables = models.ManyToManyField(
        'reservation.Table', related_name='reservations')
    booking_time = models.CharField(max_length=50, choices=[
        ("1", "15:00-17:00",),
        ("2", "16:00-18:00",),
        ("3", "17:00-19:00",),
        ("4", "18:00-20:00",),
        ("5", "19:00-21:00",),
        ("6", "20:00-22:00",),
     ])

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=50)
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


    def __str__(self):
        return f'Table {self.id}'
