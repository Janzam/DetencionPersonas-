from django.urls import path
from . import views

# Define el nombre de la aplicación para el ruteo (opcional, pero buena práctica)
app_name = 'core'

urlpatterns = [
    # path('', views.index, name='index') significa:
    # Cuando la URL sea la raíz de esta app (ej: http://127.0.0.1:8000/)
    # Llama a la función 'index' de views.py
    path('', views.index, name='index'), 
]