from django.test import TestCase
from django.urls import reverse
from .models import Table, Reservation, TABLE_TIME_CHOICES
from datetime import datetime
from django import jest


class TestReservationView(TestCase):
    def test_user_should_see_date_picker(self):
        response = self.client.get(reverse('reservation:reserve_table'))
       
        self.assertContains(response, '<div class="date-picker">')
        self.assertTemplateUsed(response, 'reservation/reservation.html')
      

class TestReservationBooking(TestCase):
    def setUp(self):
        t1 = Table.objects.create(name="t1", capacity=4)

    def test_big_party(self):
        result = Reservation.objects.make_reservation(
            name="test resv",
            number_of_persons=6,
            email='email@test.com',
            date=datetime(2022, 12, 19),
            booking_time=TABLE_TIME_CHOICES[0]
        )
        self.assertFalse(result['available'])

        t2 = Table.objects.create(name="t2", capacity=4)
  
        result = Reservation.objects.make_reservation(
            name="test resv",
            number_of_persons=6,
            email='email@test.com',
            date=datetime(2022, 12, 19),
            booking_time=TABLE_TIME_CHOICES[0]
        )
        self.assertTrue(result['available'])
        self.assertEqual(result['tables'].count(), 2)

    def test_is_table_available(self):
        result = Reservation.objects.make_reservation(
            name="test resv",
            number_of_persons=3,
            email='email@test.com',
            date=datetime(2022, 12, 19),
            booking_time=TABLE_TIME_CHOICES[0]
        )
        self.assertTrue(result['available'])
        self.assertEqual(result['tables'].first().name, "t1")

        result = Reservation.objects.make_reservation(
             name="second resv",
             number_of_persons=3,
             email='email@test.com',
             date=datetime(2022, 12, 19),
             booking_time=TABLE_TIME_CHOICES[0]
         )

        self.assertFalse(result['available'])
