from django.shortcuts import render,get_object_or_404,redirect
from .models import Room
from .forms import RoomForm
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

def createRoom(request):
    form = RoomForm
    
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        
    context = {'form':form}
    return render(request,'main/room_form.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST": 
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')   
    context = {'form':form}
    return render(request,'main/room_form.html',context)

def Delete(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request,'main/delete.html',{'obj':room})
