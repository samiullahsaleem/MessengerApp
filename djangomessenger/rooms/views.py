from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def rooms(request):
    rooms = models.Room.objects.all()
    return render(request, 'rooms/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = models.Room.objects.get(slug=slug)
    return render(request, 'rooms/room.html', {'room': room})