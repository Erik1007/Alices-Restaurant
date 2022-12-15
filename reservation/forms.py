from django import forms
from .models import Reservation
from .models import TableBooking
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    TimePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "number_of_persons", "date",] #time
        widgets = {
            "date": DatePickerInput(),
        #    "time": TimePickerInput(),
        }


class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['table_number', 'booking_time']
        widgets = {
            'booking_time': forms.RadioSelect()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table_number'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['booking_time'].widget = forms.ListBox(
            attrs={"size": len(AVAILABLE_TIMES)})
    
    def clean(self):
        cleaned_data = super().clean()
        table_number = cleaned_data.get("table_number")
        booking_time = cleaned_data.get("booking_time")
        if TableBooking.objects.filter(
                table_number=table_number, booking_time=booking_time).exists():
            raise forms.ValidationError(
                "This table is already booked for the selected time. Please choose a different table or time.")

        return cleaned_data



# class ReservationTime(forms.Form):
#     Format: (time, display_text)
#     timeSlots = [
#        ("15:00-17:00", "15:30-17:30"),
#        ("16:00-18:00", "16:30-18:30"),
#        ("17:00-19:00", "17:30-19:30"),
#        ("18:00-20:00", "18:30-20:30"),
#        ("19:00-21:00", "19:30-21:30"),
#        ("20:00-22:00", "20:30-22:30"),
#        ("21:00-23:00"),
#     ]

    # available_times = forms.ChoiceField(
    #    choices=AVAILABLE_TIMES,
    #    widget=forms.ListBox(attrs={"size": len(AVAILABLE_TIMES)})
     #)