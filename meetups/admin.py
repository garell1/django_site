from django.contrib import admin

from .models import Meetup
# Register your models here.


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'location')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    #ordering = ('-date',)
