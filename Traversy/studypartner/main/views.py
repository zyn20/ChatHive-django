from django.shortcuts import render,get_object_or_404
from .models import Room

# rooms = [
#     { 'id': 1, 'name': 'Python Programming' },
#     { 'id': 2, 'name': 'Java Programming' },
#     { 'id': 3, 'name': 'Ruby Programming' },
#     { 'id': 4, 'name': 'C++ Programming' },
#     { 'id': 5, 'name': 'C# Programming' },
#     { 'id': 6, 'name': 'Go Programming' },
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'main/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = get_object_or_404(Room, id=pk)
    context = {'room': room}
    return render(request, 'main/room.html', context)
