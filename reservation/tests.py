from django.test import TestCase
from django.urls import reverse
from .models import Table, Reservation, TABLE_TIME_CHOICES
from datetime import datetime
from django import jest


class TestReservationView(TestCase):
    """
    Test cases for reservation views.

    Inherits from:
        django.test.TestCase

    Methods:
        test_user_should_see_date_picker: Test that the user can see the date picker.
    """
    def test_user_should_see_date_picker(self):
        """
        Test that the user can see the date picker.

        Checks if the response contains the expected HTML element for the date picker
        and if the expected template is used.
        """
        response = self.client.get(reverse('reservation:reserve_table'))
       
        self.assertContains(response, '<div class="date-picker">')
        self.assertTemplateUsed(response, 'reservation/reservation.html')
      

class TestReservationBooking(TestCase):
    """
    Test cases for reservation booking.

    Inherits from:
        django.test.TestCase

    Methods:
        setUp: Set up the test data.
        test_big_party: Test booking a reservation for a big party.
        test_is_table_available: Test if a table is available for booking.
    """
    def setUp(self):
        """
        Set up the test data.

        Creates a table for testing.
        """
        t1 = Table.objects.create(name="t1", capacity=4)

    def test_big_party(self):
        """
        Test booking a reservation for a big party.

        Checks if the reservation is available when the party size exceeds the table capacity,
        and if the reservation is successfully booked when there are enough tables available.
        """
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
        """
        Test if a table is available for booking.

        Checks if a table is available when the party size is within the table capacity,
        and if a table is not available when all tables are fully booked.
        """
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
