from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import ReservationForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse
from .models import Reservation
from django.contrib import messages
from django.http import HttpResponseRedirect
import uuid


# This is the Reservation Creation and Reading section


def reserve_table(request):
    new_reservation = {}
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():          
            reservation_date = form.cleaned_data['date']         

            bad_reservation = False
            if reservation_date < timezone.now().date():
                messages.warning(
                    request, "Reservation date cannot be in the past.")
                bad_reservation = True
           
            if form.cleaned_data['number_of_persons'] < 1:
                messages.warning(
                    request, "Reservation must be at least one person.")
                bad_reservation = True

            if bad_reservation:
                context = {'form': form, "new_reservation": new_reservation}
                return render(request, 'reservation/reservation.html', context)
            
            new_reservation = Reservation.objects.make_reservation(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['number_of_persons'],
                form.cleaned_data['date'],
                form.cleaned_data['booking_time'])
            if new_reservation['available']:
                url = reverse(
                    'reservation_details', args=[new_reservation[
                        'reservation_id']])
                return redirect(url)

            else:
                context = {'form': form, "new_reservation": new_reservation}
                messages.warning(
                    request, "There are no tables available at this time for this number of people")
                return render(request, 'reservation/reservation.html', context)                
            
    else:
        form = ReservationForm()
    context = {'form': form, "new_reservation": new_reservation}
    return render(request, 'reservation/reservation.html', context)


def confirm_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    return render(
        request, 'reservation_details.html', {'reservation': reservation})


def my_booking(request):
    return render(request, 'search_reservations.html')


def reservation_details(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservation_details.html', {'reservation': reservation})

# This is the Researvation Update section


def search_reservation(request):
    if request.method == 'POST':
        reservation_name = request.POST.get('reservation_name')
        reservation = get_object_or_404(Reservation, name=reservation_name)
        reservation_id = request.POST.get('reservation_id')
        reservation = get_object_or_404(Reservation, id=reservation_id)
        return render(
            request, 'reservation_details.html', {'reservation': reservation})
    else:
        return render(request, 'search_reservation.html')


def update_reservation(request, reservation_id):
    existing_reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=existing_reservation)
        if form.is_valid():
            form.save()

            # Create a new reservation
            new_reservation = reserve_table(request)

            # Delete the existing reservation if a new reservation is created
            if new_reservation['available']:
                delete_reservation(
                    request, reservation_id=existing_reservation.id)
            return redirect(
                'reservation_details.html', reservation_id=new_reservation[
                    'reservation_id'])
    else:
        form = ReservationForm(instance=existing_reservation)
    return render(
        request, 'reservation_details.html', {
            'form': form, 'reservation': existing_reservation})

# This is the Delete Reservation section:


def delete_reservation(request):
    if request.method == 'POST':
        reservation_id = request.POST["reservation_id"]
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation.delete()
    return render(request, 'delete_reservation.html')


def table_booking(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservationModal')
    else:
        form = TableForm()

    return render(request, 'reservation/failure.html', {'form': form})
