from django.contrib import admin

from .models import (
    Meetup, 
    Location,
    Participant
)
# Register your models here.


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
  #  list_display = ('title', 'date', 'location')
    search_fields = ('title', 'location')
   # list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}
   # ordering = ('-date',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Participant)
class Participant(admin.ModelAdmin):
    list_display = ('email',)
    