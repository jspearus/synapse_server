import json

from django.shortcuts import render

from web.consumers import ChatRoomConsumer, get_device_list

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
    auto = get_rem_auto()
    auto = f"Auto: {auto}"
    weather = update_weather()
    command = get_rem__pre_command()
    command = f"Pre Command: {command}"
    event = get_next_event()
    event = f"Next Event: {event}"
    mode = get_rem_mode()
    mode = f"Mode: {mode}"

    return render(request, 'remote.html', {
        'auto': auto,
        'weather': weather,
        'command': command,
        'event': event,
        'mode': mode,
    })


def room(request):
    auto = get_rem_auto()
    auto = f"Auto: {auto}"
    weather = update_weather()
    command = get_rem__pre_command()
    event = get_next_event()

    return render(request, 'room.html', {
        'auto': auto,
        'weather': weather,
        'command': command,
        'event': event,
    })


def term(request):
    return render(request, 'term.html', {
        'room_name': 'term'
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
