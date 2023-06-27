from django.urls import re_path
from color_app.consumers import ColorConsumer

websocket_urlpatterns = [
    re_path(r'wss/color/$', ColorConsumer.as_asgi()),
]
