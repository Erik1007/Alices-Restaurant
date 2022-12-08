from django import forms
# from .models import Event
from .models import Reservation
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    TimePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
    YearPickerInput
)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "number_of_persons",]
#       widgets = {
#            "start_date": DatePickerInput(),
#            "end_date": DatePickerInput(range_from="start_date"),
#            "start_time": TimePickerInput(),
#            "end_time": TimePickerInput(range_from="start_time"),
#        }


#class ReserveTableForm(forms.ModelForm):
#    class Meta:
#        model = Reservation
#        fields = '__all__'     
