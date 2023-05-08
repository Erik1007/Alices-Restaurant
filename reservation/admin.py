from django.contrib import admin
from django.db.models import Case, When, F, BooleanField, Count
from .models import Customer, Reservation, Table


class AdminReservation(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'booking_time', 'number_of_persons')
    search_fields = ['name', 'email', 'id']
    
    def save_model(self, request, obj, form, change):
        obj.save(using=self._db)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(used_tables=Count('tables'))
        qs = qs.annotate(is_available=Case(
            When(used_tables__gte=F('number_of_persons') / 4, then=False),
            default=True,
            output_field=BooleanField(),
        ))
        return qs
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def delete_model(self, request, obj):
        obj.tables.clear()
        obj.delete()
        
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.tables.clear()
            obj.delete()

    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.tables.clear()
            obj.delete()


class AdminTable(admin.ModelAdmin):
    list_display = [
        'name',
        'capacity',
    ]


admin.site.register(Reservation, AdminReservation)
admin.site.register(Table, AdminTable)


def approve_reservation(self, request, queryset):
    queryset.update(approved=True)
