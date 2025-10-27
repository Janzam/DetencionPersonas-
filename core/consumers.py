import json
import cv2
import numpy as np
import base64
from channels.generic.websocket import WebsocketConsumer
import threading
import time
from ultralytics import YOLO 


try:
    model = YOLO('yolov8n.pt') 
except ImportError:
    print("ERROR: La librería ultralytics no está instalada. Ejecuta 'pip install ultralytics' para instalarla o ejecutar el requirements.txt.")
    model = None


is_processing = False

class VideoProcessingConsumer(WebsocketConsumer):
    def connect(self):
        self.accept() 
        global is_processing
        print("WebSocket conectado. Iniciando thread de procesamiento.")
        
      
        self.processing_thread = threading.Thread(target=self.video_stream_loop) # Crea un hilo para el procesamiento de video
        self.processing_thread.start() 

    def disconnect(self, close_code):
        global is_processing
        is_processing = False 
        print("WebSocket desconectado. Deteniendo thread.")

    def video_stream_loop(self):
        global is_processing 
        
        if model is None:
            print("No se puede iniciar el procesamiento: Modelo YOLO no disponible.")
            return

        is_processing = True

        cap = cv2.VideoCapture(0)

        while is_processing and cap.isOpened():
            ret, frame = cap.read() 
            if not ret:
                print("No se puede recibir el fotograma.")
                break
            
            frame_resized = cv2.resize(frame, (640, 480)) 
            
           
            results = model(frame_resized, classes=0, verbose=False)
            person_count = 0 
            

            for r in results:
                person_count = len(r.boxes)
                
                for box in r.boxes.xyxy:
                
                    x1, y1, x2, y2 = map(int, box.tolist())
                    
                
                    cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
        
            cv2.putText(frame_resized, 
                        f'Personas: {person_count}', 
                        (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1, 
                        (255, 0, 0), 
                        2) 
            
           
            ret, buffer = cv2.imencode('.jpg', frame_resized)
            frame_base64 = base64.b64encode(buffer).decode('utf-8') 
            self.send(text_data=json.dumps({ 
                'image': frame_base64,
                'count': person_count
            }))
            

            time.sleep(0.05) 
        
        cap.release()
        print("Procesamiento de video finalizado.")
        
    def receive(self, text_data):
        data = json.loads(text_data)
        global is_processing
        
        if 'command' in data: 
            is_processing = data['command'] == 'start'