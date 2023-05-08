from collections import namedtuple
from datetime import date, timedelta, datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
import math
import uuid


class Customer(models.Model):
    name = models.CharField(max_length=100)
    emai = models.EmailField(max_length=200)
    number_of_persons = models.PositiveIntegerField()

    def clean(self):
        if self.number_of_persons <= 0:
            raise ValueError("Number of customers must be larger than 0")
        if self.number_of_persons > 15:
            raise ValidationError(
                "Sorry, we cannot seat more than 15 customers per reservation")


TABLE_TIME_CHOICES = [
    ("1", "15:00-17:00",),
    ("2", "16:00-18:00",),
    ("3", "17:00-19:00",),
    ("4", "18:00-20:00",),
    ("5", "19:00-21:00",),
    ("6", "20:00-22:00",),
    ]


class ReservationManager(models.Manager):
    def make_reservation(
            self, name, email, number_of_persons, date, booking_time):
        existing_reservations = Reservation.objects.filter(
            date=date, booking_time=booking_time)
        used_tables = existing_reservations.values('tables')
        used_table_ids = []
        for u_table in used_tables:
            used_table_ids.append(u_table['tables'])
       
        available = Table.objects.exclude(id__in=used_table_ids)
        if available.count() == 0:
            return {'available': False}
        requested_tables = math.ceil(number_of_persons / 4.0)

        if available.count() < requested_tables:
            return {'available': False}
        new_reservation = Reservation(
            name=name,
            email=email,
            number_of_persons=number_of_persons,
            date=date,
            booking_time=booking_time)
        new_reservation.save()

        for a_table in available[:requested_tables]:
            new_reservation.tables.add(a_table)
        new_reservation.save()
        
        is_available = False
        tables = []

        return {
            "available": True,
            "tables": new_reservation.tables
        }


class Reservation(models.Model):
    reservation_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, default='example@example.com')
    number_of_persons = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)
    tables = models.ManyToManyField(
        'reservation.Table', related_name='reservations')
    booking_time = models.CharField(
        max_length=50, default=1, choices=TABLE_TIME_CHOICES)

    objects = ReservationManager()

    def save(self, *args, **kwargs):
        if not self.reservation_id:
            self.id = self.generate_reservation_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.reservation_id})'
        

class Table(models.Model):
    name = models.CharField(max_length=50, default='placeholder')
    capacity = models.IntegerField()

    def __str__(self):
        return f'Table {self.id}'

