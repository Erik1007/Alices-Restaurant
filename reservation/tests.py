from django.test import TestCase
from django.urls import reverse


class TestReservationView(TestCase):
    def test_user_should_see_date_picker(self):
        response = self.client.get(reverse('reservation:reserve_table'))
        self.assertContains(response, '<div class="date-picker">')
        
        self.assertTemplateUsed(response, 'reservation/reservation.html')

    def test_user_can_select_a_date_from_the_reservaton_form(self):
        response = self.client.post(reverse('reservation:reserve_Table'))
        self.assertContains(response, '<form>')

        self.assertEquals(response, )
        
    def test_user_can_submit_name_and_number_of_people(self):
        response = self.client.post(reverse('reservation:reserve_table'))

        self.assertContains(response, 'submit')
        self.assertTemplateUsed(response, 'reservation/reservation.html')