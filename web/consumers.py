import json
from channels.generic.websocket import AsyncWebsocketConsumer

device_list = ['all', ]


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
        message = text_data_json['message']
        username = text_data_json['username']
        destination = text_data_json['destination']
        if message == 'connected':
            if username not in device_list:
                device_list.append(username)
                print(device_list)
        elif message == 'close':
            if username in device_list:
                device_list.remove(username)
                print(device_list)
        elif message == 'devices':
            if username in device_list:
                await self.send(text_data=json.dumps({
                    'message': device_list,
                    'username': destination,
                    'destination': username,
                }))

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
                'destination': destination,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        dest = event['destination']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'destination': dest,
        }))
    pass
