from channels.generic.websocket import AsyncWebsocketConsumer

class ColorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'color_group'
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
        # Receive message from WebSocket
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'color_message',
                'message': text_data
            }
        )

    async def color_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=event['message'])
