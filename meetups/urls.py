from django.urls import path

from . import views


urlpatterns = [
    path('meetups/', views.starting_page, name='all-meetups'),
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='meetup-confirm'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),
]
