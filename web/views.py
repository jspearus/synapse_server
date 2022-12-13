import json

from django.shortcuts import render

from web.consumers import ChatRoomConsumer, get_device_list
from web.consumers import get_tree_auto_status, get_tree_status, get_village_status, get_trees_status
from web.consumers import get_carol_auto_status ,get_monitor_status,  get_street_light_status
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
    trees = get_trees_status()
    trees = f"Trees: {trees}"
    village = get_village_status()
    village = f"Village: {village}"
    tree = get_tree_status()
    tree = f"Tree: {tree}"
    strLights = get_street_light_status()
    strLights = f"Lights: {strLights}"
    tAuto = get_tree_auto_status()
    tAuto = f"Auto: {tAuto}"
    cAuto = get_carol_auto_status()
    cAuto = f"Auto: {cAuto}"
    
    if monisOn == "Off":
        mon = 'Mon: Off'
        
    elif monisOn == "On":
        mon = 'Mon: On'
    
    return render(request, 'home.html', {
        'monisOn': mon,
        'condition': condition,
        'light_status': strLights,
        'trees_status': trees,
        'tree_status': tree,
        'village_status': village,
        'cauto_status': cAuto,
        'tauto_status': tAuto
    })

def remote(request):
    
    return render(request, 'remote.html', {
        'auto': "Auto: N-A",
        'weather': "Condition: N-A",
        'command': "Pre Command: N-A",
        'event': "Next Event: N-A",
    })


def term(request, room_name):
    return render(request, 'term.html', {
        'room_name': room_name
    })
    
def hook(request, username, msg, dest):
    
    tmsg = {'message': msg,
           'username': username,
           'destination': dest}
    jmsg = json.dumps(tmsg)
    print(f"message::: {tmsg}")
    return render(request, 'hook.html', {
        'username': username,
        'msg': msg,
        'dest': dest,
    })
