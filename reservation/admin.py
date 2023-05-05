from django.contrib import admin
from .models import Customer, Reservation, Table


class AdminReservation(admin.ModelAdmin):
    list_display = [
        'name', 'email', 'number_of_persons', 'reservation_id',
    ]
    list_filter = [
        'date', 'booking_time', 'reservation_id',
    ]
    actions = ['approve_reservation', 'delete_reservation']


class AdminTable(admin.ModelAdmin):
    list_display = [
        'name',
        'capacity',
    ]


admin.site.register(Reservation, AdminReservation)
admin.site.register(Table, AdminTable)


def approve_reservation(self, request, queryset):
    queryset.update(approved=True)
