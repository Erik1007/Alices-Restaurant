from django.test import TestCase
from django.urls import reverse


class TestReservationView(TestCase):
    def test_user_should_see_date_picker(self):
        response = self.client.get(reverse('reservation:reserve_table'))
       
        self.assertContains(response, '<div class="date-picker">')
        self.assertTemplateUsed(response, 'reservation/reservation.html')
      
    def test_user_can_submit_name_and_number_of_people(self):
        response = self.client.post(reverse('reservation:reserve_table'))

        self.assertContains(response, 'submit')
        self.assertTemplateUsed(response, 'reservation/reservation.html')

    def test_user_gets_confirmation_modal(self):
        response = self.client.get(reverse('<div class="confirmation">'))

        self.assertContains(response, '<div id="reseraavationmodal">')
        self.assertTempleteUsed(response, 'reservation/reservation.html')

    def test_confirm_button_connects_to_confirmation_modal(self):
        response = self.client.get(reverse('<div class="confirmation">'))

        self.assertContains(response, '<div id="confirmationmodal">')
        self.assertTempleteUsed(response, 'reservation/reservation.html')

    def test_
