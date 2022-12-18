from http import server
import json
import time
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer

from core.data_apis import get_weather, get_sunset, getNxtHoliday

device_list = ['all', 'web', ]
new_device_list = ['all', 'web', ]
monitor_status = "Off"
street_light_status = "Off"
trees_status = "Off"
village_status = "Off"
tree_status = "Off"
tree_auto_status = "Off"
carol_auto_status = "Off"

rem_auto_status = "Off"
rem_mode = "N-A"
rem_pre_command = "N-A"
rem_next_event = "N-A"


def get_rem_auto():
    global rem_auto_status
    return rem_auto_status


def get_rem_mode():
    global rem_mode
    return rem_mode


def get_rem__pre_command():
    global rem_pre_command
    return rem_pre_command


def get_next_event():
    global rem_next_event
    return rem_next_event


def get_device_list():
    global device_list
    return device_list


def get_monitor_status():
    global monitor_status
    print(f"Monitor: {monitor_status}")
    return monitor_status


def get_street_light_status():
    global street_light_status
    print(f"Street Light: {street_light_status}")
    return street_light_status


def get_tree_status():
    global tree_status
    print(f"Tree: {tree_status}")
    return tree_status


def get_trees_status():
    global trees_status
    print(f"Trees: {trees_status}")
    return trees_status


def get_village_status():
    global village_status
    print(f"Village: {village_status}")
    return village_status


def get_tree_auto_status():
    global tree_auto_status
    print(f"Tree Auto: {tree_auto_status}")
    return tree_auto_status


def get_carol_auto_status():
    global carol_auto_status
    print(f"Carol Auto: {carol_auto_status}")
    return carol_auto_status


class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'web_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        global monitor_status, street_light_status, carol_auto_status
        global tree_status, village_status, tree_auto_status
        global device_list, trees_status
        global rem_auto_status, rem_mode, rem_pre_command, rem_next_event
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message'].lower()
        username = text_data_json['username'].lower()
        destination = text_data_json['destination'].lower()

        if message == 'connected':
            if username not in device_list:
                device_list.append(username)
                print(device_list)
                destination = "web"
                message = device_list

        elif message == 'close':
            if username in device_list:
                device_list.remove(username)
                print(device_list)
                destination = "web"
                message = device_list

        # todo update device list before sending
        elif message == 'remauto:true':
            if username == 'remote':
                if destination == 'web':
                    rem_auto_status = "On"

        elif message == 'remauto:false':
            if username == 'remote':
                if destination == 'web':
                    rem_auto_status = "Off"

        elif 'remnextevent' in message:
            if username == 'remote':
                if destination == 'web':
                    msg = message.split(':')
                    rem_next_event = f"{msg[1]} : {msg[2]}"

        elif 'remcomm' in message:
            if username == 'remote':
                if destination == 'web':
                    msg = message.split(':')
                    rem_pre_command = f"{msg[1]}"

        elif 'remmode' in message:
            if username == 'remote':
                if destination == 'web':
                    msg = message.split(':')
                    rem_mode = f"{msg[1]}"

        elif message == 'devices':
            if username in device_list:
                message = device_list
                username = username
                destination = destination

        elif message == 'weather':
            if username in device_list:
                msg = get_weather().lower()

                message = msg
                username = username
                destination = destination

        elif message == 'sunset':
            if username in device_list:
                msg = get_sunset()
                msg = "sunset:"+msg

                message = msg
                username = username
                destination = destination

        elif message == 'holiday':
            if username in device_list:
                print("Getting holiday")
                msg = getNxtHoliday().lower()
                message = msg
                username = username
                destination = username

        elif message == 'mon:true':
            if username == 'foyer':
                if destination == 'web':
                    monitor_status = "On"
                    print(f"MonOn: {monitor_status}")

        elif message == 'mon:false':
            if username == 'foyer':
                if destination == 'web':
                    monitor_status = "Off"
                    print(f"MonOn: {monitor_status}")

        elif message == 'trees:true':
            if username == 'foyer':
                if destination == 'web':
                    trees_status = "On"
                    print(f"Tree: {trees_status}")

        elif message == 'trees:false':
            if username == 'foyer':
                if destination == 'web':
                    trees_status = "Off"
                    print(f"Tree: {trees_status}")

        elif message == 'lights:false':
            if username == 'foyer':
                if destination == 'web':
                    street_light_status = "Off"
                    trese_status = "Off"
                    print(f"StreetLights: {street_light_status}")

        elif message == 'lights:true':
            if username == 'foyer':
                if destination == 'web':
                    street_light_status = "On"
                    trese_status = "On"
                    print(f"StreetLights: {street_light_status}")

        elif message == 'tree:true':
            if username == 'lvtree':
                if destination == 'web':
                    tree_status = "On"
                    print(f"Tree: {tree_status}")

        elif message == 'tree:false':
            if username == 'lvtree':
                if destination == 'web':
                    tree_status = "Off"
                    print(f"Tree: {tree_status}")

        elif message == 'vil:true':
            if username == 'lvtree':
                if destination == 'web':
                    village_status = "On"
                    print(f"Village: {village_status}")

        elif message == 'vil:false':
            if username == 'lvtree':
                if destination == 'web':
                    village_status = "Off"
                    print(f"Village: {village_status}")

        elif message == 'cauto:true':
            if username == 'foyer':
                if destination == 'web':
                    carol_auto_status = "On"
                    print(f"Carol Auto: {carol_auto_status}")

        elif message == 'cauto:false':
            if username == 'foyer':
                if destination == 'web':
                    carol_auto_status = "Off"
                    print(f"Carol Auto: {carol_auto_status}")

        elif message == 'tauto:true':
            if username == 'lvtree':
                if destination == 'web':
                    tree_auto_status = "On"
                    print(f"Tree Auto: {tree_auto_status}")

        elif message == 'tauto:false':
            if username == 'lvtree':
                if destination == 'web':
                    tree_auto_status = "Off"
                    print(f"Tree Auto: {tree_auto_status}")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroomMessage',
                'message': message,
                'username': username,
                'destination': destination,
            }
        )

    async def chatroomMessage(self, event):
        message = event['message']
        username = event['username']
        dest = event['destination']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'destination': dest,
        }))
    pass
