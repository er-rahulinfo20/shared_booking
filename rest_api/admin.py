
from django.contrib import admin
from .models import Client, Booking, RegularClass, MasterClass, Instructor

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'id')
    search_fields = ('name', 'email')


@admin.register(RegularClass)
class RegularClassAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'master_class', 'date', 'total_slots', 'available_slots', 'id')  # Adjust fields as needed


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'regular_class')
    list_select_related = ('client', 'regular_class')


@admin.register(MasterClass)
class MasterClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'id', 'duration')
    search_fields = ('class_name', )

@admin.register(Instructor)
class MasterClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'experience')
    search_fields = ('name', )