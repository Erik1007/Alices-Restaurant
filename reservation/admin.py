from django.contrib import admin
from .models import Customer, Reservation, Table


class AdminReservation(admin.ModelAdmin):
    list_display = [
        'name', 'number_of_persons',
    ]
    list_filter = [
        'date', 'booking_time',
    ]
    actions = ['approve_reservation']


class AdminTable(admin.ModelAdmin):
    list_display = [
        'name',
        'capacity',
    ]


admin.site.register(Reservation, AdminReservation)
admin.site.register(Table, AdminTable)


def approve_reservation(self, request, queryset):
    queryset.update(approved=True)
