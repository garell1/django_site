from django.shortcuts import render, redirect
# Create your views here.

from .models import Meetup, Participant
from .forms import RegistrationForm

def starting_page(request):
    meetups = Meetup.objects.all()
    return render(request,'meetups/index.html',{
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            return render(request, 'meetups/meetup_detail.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form,
            })
        elif request.method == 'POST':
            registration_form = RegistrationForm(request.POST)
            
            if registration_form.is_valid():
                #participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participant)
                return redirect('meetup-confirm', meetup_slug=meetup_slug)

            return render(request, 'meetups/meetup_detail.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form,
            })

    except Exception as exc:
        print(exc)
        return render(request,'meetups/meetup_detail.html', {
            'meetup_found': False,
            
        })

def confirm_registration(request, meetup_slug):
    email_org = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html',{
        'organizer_email': email_org.organizer_email
    })