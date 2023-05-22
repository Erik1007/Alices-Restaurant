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
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods


# This is the Reservation Creation and Reading section


def reserve_table(request):
    """
    Handle the reservation form submission and display reservation page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is 'POST' and the form is valid, redirect to the
    reservation details page.
    - If the request method is 'POST' and the form is invalid, render the
    reservation page with form errors.
    - If the request method is 'GET', render the reservation page.
    """
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
                    request, "Sorry, your reservation size is too large")
                return render(request, 'reservation/reservation.html', context)                
            
    else:
        form = ReservationForm()
    context = {'form': form, "new_reservation": new_reservation}
    return render(request, 'reservation/reservation.html', context)


def confirm_reservation(request, reservation_id):
    """
    Display the confirmation page for a specific reservation.

    Parameters:
    - request: The HTTP request object.
    - reservation_id: The ID of the reservation.

    Returns:
    - If the reservation with the specified ID is found, render the
    confirmation page with the reservation details.
    - If the reservation with the specified ID is not found, return a
    404 response.
    """
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    return render(
        request, 'reservation_details.html', {'reservation': reservation})


def reservation_details(request, reservation_id):
    """
    Display the details page for a specific reservation.

    Parameters:
    - request: The HTTP request object.
    - reservation_id: The ID of the reservation.

    Returns:
    - If the reservation with the specified ID is found, render the details
    page with the reservation details.
    - If the reservation with the specified ID is not found, return a
    404 response.
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(
        request, 'reservation_details.html', {'reservation': reservation})


def table_booking(request):
    """
    Handle the table booking form submission and display failure page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is 'POST' and the form is valid, redirect to the
    reservation modal page.
    - If the request method is 'POST' and the form is invalid, render the
    failure page with form errors.
    - If the request method is 'GET', render the failure page with an empty
    form.
    """
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservationModal')
    else:
        form = TableForm()

    return render(request, 'reservation/failure.html', {'form': form})


# This is the Researvation Update section

@require_http_methods(["GET", "POST"])
def search_reservation(request):
    """
    Handle the search reservation form submission and display the reservation
    details page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is 'POST' and the search query is valid, redirect
    to the reservation details page.
    - If the request method is 'POST' and the search query is invalid, render
    the search reservation page with an error message.
    - If the request method is 'GET', render the search reservation page.
    """
    if request.method == 'POST':
        search_name = request.POST.get('search_name')
        search_id = request.POST.get('search_id')

        if search_name or search_id:
            reservations = Reservation.objects

            if search_name:
                reservations = reservations.filter(name__icontains=search_name)
            
            if search_id:
                reservations = reservations.filter(id=search_id)

            if reservations:
                reservation_id = reservations[0].id
                return redirect(
                    'reservation_details', reservation_id=reservation_id)
            else:
                messages.warning(
                    request, 'Sorry, No reservation found for that info.')
        else:
            messages.warning(request, 'Please provide a search query.')

    return render(request, 'search_reservation.html')


def update_reservation(request, reservation_id):
    """
    Handle the reservation update form submission and display the reservation
    page.

    Parameters:
    - request: The HTTP request object.
    - reservation_id: The ID of the existing reservation.

    Returns:
    - If the request method is 'POST' and the form is valid, redirect to the
    reservation details page for the updated reservation.
    - If the request method is 'POST' and the form is invalid, render the
    reservation page with form errors.
    - If the request method is 'GET', render the reservation page with an
    empty form.
    """

    existing_reservation = get_object_or_404(
        Reservation, reservation_id=reservation_id)
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
                existing_reservation.delete()
                url = reverse(
                    'reservation_details', args=[new_reservation[
                        'reservation_id']])
                return redirect(url)

            else:
                context = {'form': form, "new_reservation": new_reservation}
                messages.warning(
                    request, "Sorry, your reservation size is too large")
                return render(request, 'reservation/reservation.html', context)               
            
    else:
        form = ReservationForm()
    context = {'form': form, "new_reservation": new_reservation}
    return render(request, 'reservation/reservation.html', context)


# This is the Delete Reservation section:


def delete_reservation(request):
    if request.method == 'POST':
        reservation_id = request.POST["reservation_id"]
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation.delete()
    return render(request, 'delete_reservation.html')

