from collections import namedtuple
from datetime import date, timedelta, datetime
import pytz
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError


# TimeRange = namedtuple('TimeRange', 'start end')

# def overlap(time_range_1, time_range_2):
#     latest_start = max(time_range_1.start, time_range_2.start)
#     earliest_end = min(time_range_1.end, time_range_2.end)
#     delta = (earliest_end - latest_start).days + 1
#     overlap = max(0, delta)
#     return overlap > 0


class Table(models.Model):
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return f'Table {self.id}'

    def seat_count(self):
        return self.seats.count()

    def available_seats(self):
        return self.seats.filter(occupied=False).count()


class Seat(models.Model):
    # Attributes
    occupied = models.BooleanField(default=False)

    # Relationships
    seat = models.ForeignKey(
        'reservation.Table', on_delete=models.SET_NULL, null=True, related_name='seats')


class Reservation(models.Model):
    name = models.CharField(max_length=100,)
    number_of_persons = models.IntegerField()
    email = models.CharField(max_length=150, null=True)
    date = models.DateField('Start date', default=datetime.today)
    time = models.TimeField('Start time', timezone.activate(
        pytz.timezone('CET')), default=timezone.now())
    tables = models.ManyToManyField(
        'reservation.Table', related_name='reservations')
#   is_valid = models.BooleanField(default=False)
    current_date = datetime.now()

#   Query the database for bookings that have passed
#   bookings = Reservation.objects.filter(date__lt=current_date)

#   Delete the bookings
#   bookings.delete()

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.does_not_overlap():
    #         raise ValidationError(
    #           'Reservation datetime overlaps with another reservation.')
    #     return self

    # def datetime(self):
    #     return datetime.combine(self.date, self.time)

    # def time_range(self):
    #     return TimeRange(self.datetime(), self.datetime() + timedelta(hours=2))

    # def does_not_overlap(self):
    #     reservation_doesnt_overlap = True
    #     for table in self.tables.all():
    #         for reservation in table.reservations.exclude(
    #           id=self.id).filter(date=self.date):
    #             if overlap(self.time_range(), reservation.time_range()):
    #                 reservation_doesnt_overlap = False
    #     return reservation_doesnt_overlap


class Customer():
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()


