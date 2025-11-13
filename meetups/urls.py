from django.urls import path

from . import views


urlpatterns = [
    path('meetups/', views.starting_pager),
    path('meetups/<slug:meetup_slug>', views.meetup_details)
]
