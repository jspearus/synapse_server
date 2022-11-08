from django.shortcuts import render

from web.consumers import get_device_list, get_monitor_status


def dashboard(request):
    devices = get_device_list()
    return render(request, 'dashboard.html', {
        'devices': devices
    })

def home(request):
    monStat = get_monitor_status()
    print(monStat)
    if monStat == False:
        mon = 'Mon: Off'
        
    elif monStat == True:
        mon = 'Mon: On'
    print(mon)
    return render(request, 'home.html', {
        'monStat': mon
    })

def remote(request):
    return render(request, 'remote.html', {})


def term(request, room_name):
    return render(request, 'term.html', {
        'room_name': room_name
    })
