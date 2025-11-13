from django.urls import path

from . import views


urlpatterns = [
    path('meetups/', views.starting_pager, name='all-meetups'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]
