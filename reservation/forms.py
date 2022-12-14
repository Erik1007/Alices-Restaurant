from django import forms
from .models import Reservation
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    TimePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "number_of_persons", "date", "time"]
        widgets = {
            "date": DatePickerInput(),
            "time": TimePickerInput(),
        }


# class ReservationForm(forms.Form):
    # Define a list of tuples with the available times
    # Format: (time, display_text)
    # AVAILABLE_TIMES = [
    #    ("15:00-17:00", "15:30-17:30"),
    #    ("16:00-18:00", "16:30-18:30"),
    #    ("17:00-19:00", "17:30-19:30"),
    #    ("18:00-20:00", "18:30-20:30"),
    #    ("19:00-21:00", "19:30-21:30"),
    #    ("20:00-22:00", "20:30-22:30"),
    #    ("21:00-23:00"),
    # ]

    # Use a ChoiceField with the available times
    # time = forms.ChoiceField(
    #    choices=AVAILABLE_TIMES,
    #    widget=forms.ListBox(attrs={"size": len(AVAILABLE_TIMES)})
    # )