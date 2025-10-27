from django.shortcuts import render

def index(request):
    """
    Función de vista que maneja la petición HTTP para la página principal.
    Simplemente renderiza la plantilla HTML donde corre todo el frontend.
    """
    
    return render(request, 'index.html')

