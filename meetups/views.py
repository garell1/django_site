from django.shortcuts import render
# Create your views here.

def starting_pager(request):
    meetups = [
        {'title': "A First meetup"},
        {'title': "A Second meetup"}
    ]
    return render(request,'meetups/index.html',{
        'show'
        'meetups': meetups
    })