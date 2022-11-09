from django.shortcuts import render

from web.consumers import get_device_list, get_monitor_status
from core.data_apis import get_weather


def update_weather():
    temp = get_weather()
    if temp == 'clear':
        condition = 'Condition: Clear'
    elif temp == 'cloud':
        condition = 'Condition: Cloudy'
    elif temp == 'rain':
        condition = 'Condition: Rain'
    elif temp == 'snow':
        condition = 'Condition: Snow'
    elif temp == 'fog':
        condition = 'Condition: Fog'
        
    return condition

def dashboard(request):
    devices = get_device_list()
    return render(request, 'dashboard.html', {
        'devices': devices
    })

def home(request):
    monisOn = get_monitor_status()
    condition = update_weather()
    print(f"monReq: {monisOn}")
    if monisOn == "Off":
        mon = 'Mon: Off'
        
    elif monisOn == "On":
        mon = 'Mon: On'
        
    print(f"Mon: {mon}")
    
    return render(request, 'home.html', {
        'monisOn': mon,
        'condition': condition
    })

def remote(request):
    return render(request, 'remote.html', {})


def term(request, room_name):
    return render(request, 'term.html', {
        'room_name': room_name
    })
