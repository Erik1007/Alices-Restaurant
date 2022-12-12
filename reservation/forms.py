from django import forms
# from .models import Event
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


#class confirmPlease(forms.ModelForm):
#    class Meta:
#        model = Confirm
#        Fields = ["name", "number_of_persons", "date", "time"]
