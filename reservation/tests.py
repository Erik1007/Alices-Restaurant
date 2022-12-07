from django.test import TestCase
from django.urls import reverse


class TestReservationView(TestCase):
    def test_user_should_see_date_picker(self):
        response = self.client.get(reverse('reservation:reserve_table'))
        
        self.assertContains(response, '<div class="date-picker">')
        self.assertTemplateUsed(response, 'reservation/reservation.html')
        
