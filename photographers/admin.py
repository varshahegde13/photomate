from django.contrib import admin
from .models import Photographer, Event,Booking
# Register your models here.

admin.site.register(Photographer)
admin.site.register(Event)
admin.site.register(Booking)