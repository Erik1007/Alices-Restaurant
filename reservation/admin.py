from django.contrib import admin
from .models import Reservation, Table, Seat


class AdminReservation(admin.ModelAdmin):
    list_display = [
        'name', 'number_of_persons',
    ]
    list_filter = [
        'date', 'time',
    ]
    actions = ['approve_reservation']


admin.site.register(Reservation, AdminReservation)
admin.site.register(Table)
admin.site.register(Seat)


def approve_reservation(self, request, queryset):
    queryset.update(approved=True)
