from django.urls import re_path
from .consumers import ColorConsumer

websocket_urlpatterns = [
    re_path(r'ws/color/$', ColorConsumer.as_asgi()),
]
