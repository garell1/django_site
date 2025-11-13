from django.shortcuts import render
# Create your views here.

def starting_pager(request):
    meetups = [
        {
            'title': "A First meetup", 
            'location': 'New Your', 
            'slug': 'a-first-meetup'
        },
        {
            'title': "A Second meetup", 
            'location': 'Paris', 
            'slug': 'a-second-meetup'
        }
    ]
    return render(request,'meetups/index.html',{
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup', 
        'description': 'This is first meetup'
        }
    return render(request, 'meetups/meetup_detail.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })