from django import forms
from .models import Reservation
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'     

# class EventForm(forms.ModelForm):
#    class Meta:
#        model = Event
#        fields = [
#           "start_date", "start_time", "start_datetime", "start_month",
#           "start_year"]
#        widgets = {
#            "start_date": DatePickerInput(),
#            "start_time": TimePickerInput(),
#            "start_datetime": DateTimePickerInput(),
#            "start_month": MonthPickerInput(),
#            "start_year": YearPickerInput(),
#       }


# class EventForm(forms.ModelForm):
#    class Meta:
#        model = Event
#        fields = ["name", "start_date", "end_date", "start_time", "end_time"]
#        widgets = {
#            "start_date": DatePickerInput(),
#            "end_date": DatePickerInput(range_from="start_date"),
#            "start_time": TimePickerInput(),
#            "end_time": TimePickerInput(range_from="start_time"),
#        }
