from django.shortcuts import render
from django.views import generic
from .forms import ReservationForm
from .forms import TableBookingForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views.generic import CreateView
from django.urls import reverse_lazy


def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    context = {'form': form}
    return render(request, 'reservation/reservation.html', context)


def table_booking(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservationModal')
    else:
        form = TableBookingForm()

    return render(request, 'reservation/reservation.html', {'form': form})
