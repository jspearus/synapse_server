from http import server
import json, time, datetime
from channels.generic.websocket import AsyncWebsocketConsumer

from core.data_apis import get_weather, get_sunset, getNxtHoliday

device_list = ['all', 'web',]
new_device_list = ['all', 'web',]

    
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
        elif message == 'devices':
            if username in device_list:
                message = device_list
                username = username
                destination = destination
                
        elif message == 'weather':
            if username in device_list:
                msg=get_weather().lower()              
    
                message = msg
                username = username
                destination = destination
                
        elif message == 'sunset':
            if username in device_list:
                msg=get_sunset()
                msg ="sunset:"+msg              
    
                message = msg
                username = username
                destination = destination
                
        elif message == 'holiday':
            if username in device_list:
                print("Getting holiday")
                msg=getNxtHoliday().lower()              
    
                message = msg
                username = username
                destination = destination
                
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

