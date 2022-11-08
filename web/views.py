from django.shortcuts import render

from web.consumers import get_device_list

def dashboard(request):
    devices = get_device_list()
    return render(request, 'dashboard.html', {
        'devices': devices
    })

def home(request):
    return render(request, 'home.html', {})

def remote(request):
    return render(request, 'remote.html', {})


def term(request, room_name):
    return render(request, 'term.html', {
        'room_name': room_name
    })
