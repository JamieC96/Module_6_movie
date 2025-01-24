from django.contrib import admin
from .models import Film, Seat, Booking

admin.site.register(Film)
admin.site.register(Seat)
admin.site.register(Booking)
