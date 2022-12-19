from django import forms
from .models import Customer, Reservation, Table, TABLE_TIME_CHOICES
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        tables = forms.CharField(label='Tables', max_length=50)
        fields = ["name", "number_of_persons", "date", "booking_time"]
        widgets = {
             "date": DatePickerInput()}

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        new_reservation = Reservation()
        new_reservation.name = cleaned_data['name']
        new_reservation.number_of_persons = cleaned_data['number_of_persons']
        new_reservation.date = cleaned_data['date']
        new_reservation.time = cleaned_data['booking_time']
    
        return cleaned_data
