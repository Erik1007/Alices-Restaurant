from django.shortcuts import render, redirect
from django.views import generic
from .forms import ReservationForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Reservation


def reserve_table(request):
    new_reservation = {}
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_reservation = Reservation.objects.make_reservation(
                form.cleaned_data['name'], 
    #           form.cleaned_data['email'], 
                "placeholder@email.com",
                form.cleaned_data['number_of_persons'], 
                form.cleaned_data['date'], 
                form.cleaned_data['booking_time'])
            if new_reservation['available']:
                redirect('/success')
    else:
        form = ReservationForm()
    context = {'form': form, "new_reservation": new_reservation}
    return render(request, 'reservation/reservation.html', context)


def table_booking(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservationModal')
    else:
        form = TableForm()

    return render(request, 'reservation/reservation.html', {'form': form})


