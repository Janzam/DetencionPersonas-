import json
import cv2
import numpy as np
import base64
from channels.generic.websocket import WebsocketConsumer
import threading
import time
from ultralytics import YOLO 

# Inicializa el modelo YOLOv8nano (rápido y optimizado)
# Se carga una sola vez al iniciar el servidor
try:
    # Intenta cargar el modelo pre-entrenado
    model = YOLO('yolov8n.pt') 
except ImportError:
    print("ERROR: La librería ultralytics no está instalada. Ejecuta 'pip install ultralytics'")
    model = None

# Control global del bucle de video
is_processing = False

class VideoProcessingConsumer(WebsocketConsumer):
    """Maneja la conexión WebSocket y el procesamiento de video con YOLOv8."""
    def connect(self):
        self.accept()
        print("WebSocket conectado. Iniciando thread de procesamiento (YOLOv8).")
        
        # Iniciamos el procesamiento de video en un HILO separado para no bloquear Django
        self.processing_thread = threading.Thread(target=self.video_stream_loop)
        self.processing_thread.start()

    def disconnect(self, close_code):
        """Se llama cuando el cliente desconecta el WebSocket."""
        global is_processing
        is_processing = False # Detiene el bucle en el hilo
        print("WebSocket desconectado. Deteniendo thread.")

    def video_stream_loop(self):
        """Captura, procesa (YOLOv8) y envía frames."""
        global is_processing
        
        if model is None:
            print("No se puede iniciar el procesamiento: Modelo YOLO no disponible.")
            return

        is_processing = True

        # Captura de video: 0 para la webcam predeterminada (AJUSTA ESTE NÚMERO si no funciona)
        cap = cv2.VideoCapture(0) 

        while is_processing and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("No se puede recibir el fotograma.")
                break
            
            # Redimensionar el frame para acelerar el procesamiento de YOLO
            frame_resized = cv2.resize(frame, (640, 480))
            
            # 1. Detección con YOLOv8
            # classes=0: detecta solo la clase 'persona'
            # verbose=False: no imprime resultados en la consola por cada frame
            results = model(frame_resized, classes=0, verbose=False)
            
            person_count = 0
            
            # 2. Procesar los resultados y dibujar recuadros
            for r in results:
                person_count = len(r.boxes)
                
                # Iterar sobre las detecciones de cajas (boxes)
                for box in r.boxes.xyxy:
                    # Las coordenadas vienen como flotantes, las convertimos a enteros
                    x1, y1, x2, y2 = map(int, box) 
                    
                    # Dibujar el rectángulo (Color Verde)
                    cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 3. Poner el contador en el frame
            cv2.putText(frame_resized, 
                        f'Personas: {person_count}', 
                        (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1, 
                        (255, 0, 0), # Azul
                        2) 
            
            # 4. Codificar frame a JPEG y luego a Base64 para enviarlo por WebSocket
            ret, buffer = cv2.imencode('.jpg', frame_resized)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')

            # 5. Envío de datos al navegador
            self.send(text_data=json.dumps({
                'image': frame_base64,
                'count': person_count
            }))
            
            # Pequeña pausa para controlar la velocidad del stream
            time.sleep(0.05) 
        
        cap.release()
        print("Procesamiento de video finalizado.")
        
    def receive(self, text_data):
        # Este consumidor solo envía datos, no espera recibir mensajes del cliente.
        pass