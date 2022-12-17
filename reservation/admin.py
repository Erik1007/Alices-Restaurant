from django.contrib import admin
from .models import Customer, Reservation, Table


class AdminReservation(admin.ModelAdmin):
    list_display = [
        'email', 'number_of_persons',
    ]
    list_filter = [
        'date', 'booking_time',
    ]
    actions = ['approve_reservation']


admin.site.register(Reservation, AdminReservation)
admin.site.register(Table)
# admin.site.register(Seat)


def approve_reservation(self, request, queryset):
    queryset.update(approved=True)
