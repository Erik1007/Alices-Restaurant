from django.shortcuts import render
from django.views import generic
from reservation.models import Reservation
from .forms import ReserveTableForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}

    return render(request, 'reservation/reservation.html')


# class CreateView(generic.edit.CreateView):
#    model = Question
#    fields = ["question_text", "pub_date"]

#    def get_form(self):
#        form = super().get_form()
#        form.fields["pub_date"].widget = DateTimePickerInput()
#        return form
