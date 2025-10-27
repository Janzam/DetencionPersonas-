from django.urls import re_path

from . import consumers

# Esta lista de patrones de URL es la que busca DeteccionPersonas/asgi.py
websocket_urlpatterns = [
    # re_path(r'ws/video/$', ...) define que cualquier conexión a 
    # ws://<servidor>/ws/video/ será manejada por nuestro Consumer.
    # El "$" asegura que no haya caracteres adicionales después de 'video/'.
    re_path(r'ws/video/$', consumers.VideoProcessingConsumer.as_asgi()),
]
