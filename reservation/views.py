from django.shortcuts import render, redirect
from django.views import generic
from .forms import ReservationForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Reservation
from django.contrib import messages
from django.http import HttpResponseRedirect


def reserve_table(request):
    new_reservation = {}
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():           
            reservation_date = form.cleaned_data['date']            

            bad_reservation = False
            if reservation_date < timezone.now().date():
                messages.warning(request, "Reservation date cannot be in the past.")
                bad_reservation = True
            
            if form.cleaned_data['number_of_persons'] < 1:
                messages.warning(request, "Reservation must be at least one person.")
                bad_reservation = True

            if bad_reservation:
                context = {'form': form, "new_reservation": new_reservation}
                return render(request, 'reservation/reservation.html', context)
            
            new_reservation = Reservation.objects.make_reservation(
                form.cleaned_data['name'],
                form.cleaned_data['number_of_persons'],
                form.cleaned_data['date'],
                form.cleaned_data['booking_time'])
            if new_reservation['available']:
                messages.success(request, f"Reservation made successfully for {form.cleaned_data['number_of_persons']}") 
                #successpage/{new_reservation.id}
                return HttpResponseRedirect(request.path_info)
            else:
                #not available
                context = {'form': form, "new_reservation": new_reservation}
                messages.warning(request, "There are no tables available at this time for this number of people")
                return render(request, 'reservation/reservation.html', context)                
            
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

    return render(request, 'reservation/failure.html', {'form': form})
