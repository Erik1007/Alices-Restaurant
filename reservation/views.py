from django.shortcuts import render
from django.views import generic
from .forms import ReservationForm
# from reservation.models import Reservation
# from .forms import ReserveTableForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views.generic import CreateView
from django.urls import reverse_lazy


# class CreateView(generic.edit.CreateView):
#    model = Reservation
#    fields = ["question_text", "pub_date"]

#    def get_form(self):
#        form = super().get_form()
#        form.fields["pub_date"].widget = DateTimePickerInput()
#        return form


def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    context = {'form': form}
    return render(request, 'reservation/reservation.html', context)


# def edit_confirmation(request):
#    confirm_form = ConfirmPlease()

#    if request.method == 'POST':
#        confirm_form = ConfirmPlease(request.POST)

#        if confirm_form.is_valid():
#            confirm_form.save()
    
#    context = {'form': confirm_form}

    # return render(request, 'reservation/reservation.html', context)