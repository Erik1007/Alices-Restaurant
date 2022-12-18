from django import forms
from .models import Customer, Reservation, Table
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["number_of_persons", "date", "booking_time"]
        widgets = {
            "date": DatePickerInput(),
            "booking_time": forms.CheckboxInput(
                attrs={"size": len('booking_time')})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tables'].widget.attrs.update['class'] = 'form-control'
        self.fields['booking_time'].widget = forms.ListBox(
             attrs={"size": len(AVAILABLE_TIMES)})
    
    def clean(self):
        cleaned_data = super().clean()
        tables = cleaned_data.get("tables")
        booking_time = cleaned_data.get("booking_time")
        if Table.objects.filter(
                 table_number=table_number, booking_time=booking_time).exists():
            raise forms.ValidationError(
                 "This table is already booked for the selected time. Please choose a different table or time.")

        return cleaned_data

