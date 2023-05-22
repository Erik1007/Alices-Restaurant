from django import forms
from .models import Customer, Reservation, Table, TABLE_TIME_CHOICES
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
)


class ReservationForm(forms.ModelForm):
    """
    A form for creating or updating a reservation.

    Inherits from:
        forms.ModelForm

    Attributes:
        Meta:
            model: The model associated with the form.
            tables: The tables field in the form.
            fields: The fields displayed in the form.
            widgets: The widgets used for form fields.

    Methods:
        clean: Perform form field validation and return cleaned data.
    """
    class Meta:
        model = Reservation
        tables = forms.CharField(label='Tables', max_length=50)
        fields = ["name", "email", "number_of_persons", "date", "booking_time"]
        widgets = {
             "date": DatePickerInput()}

    def clean(self):
        """
        Clean and validate form data.

        Returns:
            dict: The cleaned form data.
        """
        cleaned_data = super().clean()
        print(cleaned_data)
        new_reservation = Reservation()
        new_reservation.name = cleaned_data['name']
        new_reservation.email = cleaned_data['email']
        new_reservation.number_of_persons = cleaned_data['number_of_persons']
        new_reservation.date = cleaned_data['date']
        new_reservation.time = cleaned_data['booking_time']
    
        return cleaned_data
