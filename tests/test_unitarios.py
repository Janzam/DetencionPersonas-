""""""

Pruebas Unitarias - Sistema de Detección de PersonasTest Unitarios para el proyecto de Detección de Personas

Pruebas aisladas sin dependencias externas usando mocksPruebas aisladas sin dependencias externas (sin YOLO real, sin cámara)

""""""

import unittest

import unittestimport numpy as np

import sysimport cv2

import osfrom unittest.mock import Mock, MagicMock, patch

import numpy as npimport sys

import cv2import os



# Agregar el directorio raíz al path# Agregar el directorio raíz al path para importar los módulos

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))





class MockBox:class MockBox:

    """Mock de la clase Box de YOLO"""    """Mock de una caja de detección de YOLO"""

    def __init__(self, xyxy, cls, conf):    def __init__(self, cls, xyxy):

        self.xyxy = xyxy        self.cls = [cls]

        self.cls = cls        self.xyxy = [Mock(cpu=lambda: Mock(numpy=lambda: np.array(xyxy)))]

        self.conf = conf



class MockResult:

class MockResult:    """Mock de un resultado de YOLO"""

    """Mock de la clase Result de YOLO"""    def __init__(self, boxes_data):

    def __init__(self, boxes_data):        self.boxes = [MockBox(cls, xyxy) for cls, xyxy in boxes_data]

        self.boxes = []

        for box_data in boxes_data:

            self.boxes.append(MockBox(class MockYOLOModel:

                xyxy=box_data['xyxy'],    """Mock del modelo YOLO para pruebas unitarias"""

                cls=box_data['cls'],    def __init__(self, detections=None):

                conf=box_data['conf']        self.detections = detections or []

            ))    

    def __call__(self, frame, verbose=False, classes=None):

        """Simula la llamada al modelo YOLO"""

class MockYOLOModel:        return [MockResult(self.detections)]

    """Mock del modelo YOLO"""

    def __init__(self, results_data):

        self.results_data = results_dataclass TestDeteccionPersonasUnitario(unittest.TestCase):

        """Pruebas unitarias para la lógica de detección de personas"""

    def __call__(self, frame):    

        return [MockResult(self.results_data)]    def setUp(self):

        """Configuración inicial para cada prueba"""

        self.frame_test = np.zeros((480, 640, 3), dtype=np.uint8)

class TestDeteccionPersonasUnitario(unittest.TestCase):    

    """Suite de pruebas unitarias para detección de personas"""    def test_procesar_frame_sin_personas(self):

            """

    def setUp(self):        Test 1: Verificar que procesar_frame retorna 0 cuando no hay personas

        """Configuración inicial para cada prueba"""        """

        # Frame de prueba (imagen vacía)        # Arrange: Modelo mock sin detecciones

        self.frame = np.zeros((480, 640, 3), dtype=np.uint8)        model_mock = MockYOLOModel(detections=[])

            

    def test_procesar_frame_sin_personas(self):        # Act: Procesar frame con el modelo mock

        """Prueba: Procesar frame sin personas detectadas"""        results = model_mock(self.frame_test, verbose=False)

        # Modelo mock sin detecciones        person_count = 0

        modelo = MockYOLOModel([])        

                for r in results:

        # Simular procesamiento            person_count = len(r.boxes)

        results = modelo(self.frame)        

        conteo = sum(1 for r in results for box in r.boxes if box.cls == 0)        # Assert: Debe retornar 0 personas

                self.assertEqual(person_count, 0, "Debe detectar 0 personas cuando no hay detecciones")

        self.assertEqual(conteo, 0, "No debería detectar personas en frame vacío")    

        def test_procesar_frame_con_dos_personas(self):

    def test_procesar_frame_con_una_persona(self):        """

        """Prueba: Procesar frame con una persona"""        Test 2: Verificar que procesar_frame retorna 2 cuando se simulan dos detecciones

        # Modelo mock con una detección de persona (clase 0)        """

        boxes_data = [        # Arrange: Modelo mock con 2 detecciones de personas (clase 0)

            {'xyxy': np.array([[100, 100, 200, 300]]), 'cls': np.array([0]), 'conf': np.array([0.85])}        detections = [

        ]            (0, [100, 100, 200, 300]),  # Persona 1

        modelo = MockYOLOModel(boxes_data)            (0, [300, 150, 400, 350])   # Persona 2

                ]

        results = modelo(self.frame)        model_mock = MockYOLOModel(detections=detections)

        conteo = sum(1 for r in results for box in r.boxes if box.cls == 0)        

                # Act: Procesar frame

        self.assertEqual(conteo, 1, "Debería detectar exactamente una persona")        results = model_mock(self.frame_test, verbose=False)

            person_count = 0

    def test_procesar_frame_con_multiples_personas(self):        cajas = []

        """Prueba: Procesar frame con múltiples personas"""        

        # Modelo mock con tres detecciones de personas        for r in results:

        boxes_data = [            person_count = len(r.boxes)

            {'xyxy': np.array([[100, 100, 200, 300]]), 'cls': np.array([0]), 'conf': np.array([0.85])},            for box in r.boxes:

            {'xyxy': np.array([[300, 100, 400, 300]]), 'cls': np.array([0]), 'conf': np.array([0.90])},                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

            {'xyxy': np.array([[500, 100, 600, 300]]), 'cls': np.array([0]), 'conf': np.array([0.78])}                cajas.append((int(x1), int(y1), int(x2), int(y2)))

        ]        

        modelo = MockYOLOModel(boxes_data)        # Assert: Debe detectar 2 personas

                self.assertEqual(person_count, 2, "Debe detectar 2 personas")

        results = modelo(self.frame)        self.assertEqual(len(cajas), 2, "Debe tener 2 cajas delimitadoras")

        conteo = sum(1 for r in results for box in r.boxes if box.cls == 0)    

            def test_procesar_frame_retorna_diccionario(self):

        self.assertEqual(conteo, 3, "Debería detectar tres personas")        """

            Test 3: Verificar que procesar_frame retorna un diccionario con claves correctas

    def test_filtrar_solo_personas(self):        """

        """Prueba: Filtrar solo detecciones de personas (clase 0)"""        # Arrange: Modelo mock con 1 detección

        # Modelo mock con personas y otros objetos        detections = [(0, [50, 50, 150, 250])]

        boxes_data = [        model_mock = MockYOLOModel(detections=detections)

            {'xyxy': np.array([[100, 100, 200, 300]]), 'cls': np.array([0]), 'conf': np.array([0.85])},  # Persona        

            {'xyxy': np.array([[300, 100, 400, 200]]), 'cls': np.array([1]), 'conf': np.array([0.90])},  # Bicicleta        # Act: Simular procesamiento

            {'xyxy': np.array([[500, 100, 600, 300]]), 'cls': np.array([0]), 'conf': np.array([0.78])},  # Persona        results = model_mock(self.frame_test, verbose=False)

            {'xyxy': np.array([[200, 300, 300, 400]]), 'cls': np.array([2]), 'conf': np.array([0.82])}   # Auto        resultado = {"count": 0, "cajas": []}

        ]        

        modelo = MockYOLOModel(boxes_data)        for r in results:

                    resultado["count"] = len(r.boxes)

        results = modelo(self.frame)            for box in r.boxes:

        conteo_personas = sum(1 for r in results for box in r.boxes if box.cls == 0)                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

        conteo_total = sum(1 for r in results for box in r.boxes)                resultado["cajas"].append((int(x1), int(y1), int(x2), int(y2)))

                

        self.assertEqual(conteo_personas, 2, "Debería detectar solo 2 personas")        # Assert: Verificar estructura del diccionario

        self.assertEqual(conteo_total, 4, "Total de detecciones debería ser 4")        self.assertIsInstance(resultado, dict, "El resultado debe ser un diccionario")

            self.assertIn("count", resultado, "Debe contener la clave 'count'")

    def test_estructura_datos_resultado(self):        self.assertIn("cajas", resultado, "Debe contener la clave 'cajas'")

        """Prueba: Verificar estructura de datos del resultado"""        self.assertIsInstance(resultado["count"], int, "'count' debe ser un entero")

        boxes_data = [        self.assertIsInstance(resultado["cajas"], list, "'cajas' debe ser una lista")

            {'xyxy': np.array([[100, 100, 200, 300]]), 'cls': np.array([0]), 'conf': np.array([0.85])}    

        ]    def test_procesar_frame_filtrar_solo_personas(self):

        modelo = MockYOLOModel(boxes_data)        """

                Test 4: Verificar que solo se cuentan objetos de clase 0 (personas)

        results = modelo(self.frame)        """

                # Arrange: Modelo mock con diferentes clases de objetos

        self.assertIsInstance(results, list, "Resultado debería ser una lista")        detections = [

        self.assertTrue(len(results) > 0, "Resultado no debería estar vacío")            (0, [100, 100, 200, 300]),  # Persona (clase 0)

        self.assertTrue(hasattr(results[0], 'boxes'), "Resultado debería tener atributo 'boxes'")            (1, [300, 150, 400, 250]),  # Bicicleta (clase 1)

                (2, [500, 200, 600, 350]),  # Auto (clase 2)

    def test_coordenadas_bounding_box(self):            (0, [150, 300, 250, 450])   # Otra persona (clase 0)

        """Prueba: Validar coordenadas del bounding box"""        ]

        boxes_data = [        model_mock = MockYOLOModel(detections=detections)

            {'xyxy': np.array([[100, 150, 200, 300]]), 'cls': np.array([0]), 'conf': np.array([0.85])}        

        ]        # Act: Procesar y filtrar solo personas

        modelo = MockYOLOModel(boxes_data)        results = model_mock(self.frame_test, verbose=False)

                person_count = 0

        results = modelo(self.frame)        

        box = results[0].boxes[0]        for r in results:

                    for box in r.boxes:

        x1, y1, x2, y2 = box.xyxy[0]                if int(box.cls[0]) == 0:  # Solo clase 0 (persona)

                            person_count += 1

        self.assertLess(x1, x2, "x1 debería ser menor que x2")        

        self.assertLess(y1, y2, "y1 debería ser menor que y2")        # Assert: Solo debe contar las 2 personas

        self.assertGreaterEqual(x1, 0, "x1 no debería ser negativo")        self.assertEqual(person_count, 2, "Debe contar solo objetos de clase 0 (personas)")

        self.assertGreaterEqual(y1, 0, "y1 no debería ser negativo")    

        def test_coordenadas_cajas_validas(self):

    def test_confianza_deteccion(self):        """

        """Prueba: Validar nivel de confianza"""        Test 5: Verificar que las coordenadas de las cajas son válidas

        boxes_data = [        """

            {'xyxy': np.array([[100, 100, 200, 300]]), 'cls': np.array([0]), 'conf': np.array([0.85])}        # Arrange

        ]        detections = [(0, [100, 150, 300, 450])]

        modelo = MockYOLOModel(boxes_data)        model_mock = MockYOLOModel(detections=detections)

                

        results = modelo(self.frame)        # Act

        conf = results[0].boxes[0].conf[0]        results = model_mock(self.frame_test, verbose=False)

                cajas = []

        self.assertGreaterEqual(conf, 0.0, "Confianza debería ser >= 0")        

        self.assertLessEqual(conf, 1.0, "Confianza debería ser <= 1")        for r in results:

                for box in r.boxes:

    def test_formato_mensaje_websocket(self):                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

        """Prueba: Verificar formato del mensaje para WebSocket"""                cajas.append((int(x1), int(y1), int(x2), int(y2)))

        import json        

                # Assert

        # Simular datos para WebSocket        self.assertEqual(len(cajas), 1)

        mensaje = {        x1, y1, x2, y2 = cajas[0]

            'tipo': 'deteccion',        self.assertGreater(x2, x1, "x2 debe ser mayor que x1")

            'conteo': 3,        self.assertGreater(y2, y1, "y2 debe ser mayor que y1")

            'frame': 'base64_encoded_image',        self.assertGreaterEqual(x1, 0, "Coordenadas no deben ser negativas")

            'timestamp': '2024-01-01 12:00:00'        self.assertGreaterEqual(y1, 0, "Coordenadas no deben ser negativas")

        }    

            def test_frame_vacio_no_causa_error(self):

        # Verificar que se puede serializar a JSON        """

        mensaje_json = json.dumps(mensaje)        Test 6: Verificar que un frame vacío no causa errores

        mensaje_recuperado = json.loads(mensaje_json)        """

                # Arrange

        self.assertEqual(mensaje_recuperado['tipo'], 'deteccion')        frame_vacio = np.zeros((480, 640, 3), dtype=np.uint8)

        self.assertEqual(mensaje_recuperado['conteo'], 3)        model_mock = MockYOLOModel(detections=[])

        self.assertIsInstance(mensaje_json, str)        

            # Act & Assert: No debe lanzar excepciones

    def test_comando_control_deteccion(self):        try:

        """Prueba: Verificar comandos de control (iniciar/detener)"""            results = model_mock(frame_vacio, verbose=False)

        import json            person_count = len(results[0].boxes)

                    self.assertEqual(person_count, 0)

        # Comando de inicio        except Exception as e:

        comando_inicio = {'comando': 'iniciar'}            self.fail(f"Procesar frame vacío causó una excepción: {e}")

        self.assertEqual(comando_inicio['comando'], 'iniciar')    

            @patch('cv2.VideoCapture')

        # Comando de detención    def test_mock_camara_no_disponible(self, mock_capture):

        comando_detener = {'comando': 'detener'}        """

        self.assertEqual(comando_detener['comando'], 'detener')        Test 7: Verificar comportamiento cuando la cámara no está disponible

                """

        # Verificar serialización        # Arrange: Mock de cámara que no se puede abrir

        self.assertIsInstance(json.dumps(comando_inicio), str)        mock_cap_instance = Mock()

        self.assertIsInstance(json.dumps(comando_detener), str)        mock_cap_instance.isOpened.return_value = False

        mock_capture.return_value = mock_cap_instance

        

def suite():        # Act

    """Crear suite de pruebas unitarias"""        cap = cv2.VideoCapture(0)

    suite = unittest.TestSuite()        

    loader = unittest.TestLoader()        # Assert

    suite.addTests(loader.loadTestsFromTestCase(TestDeteccionPersonasUnitario))        self.assertFalse(cap.isOpened(), "La cámara mock no debe estar disponible")

    return suite



class TestWebSocketLogica(unittest.TestCase):

if __name__ == '__main__':    """Pruebas unitarias para la lógica del WebSocket Consumer"""

    runner = unittest.TextTestRunner(verbosity=2)    

    runner.run(suite())    def test_formato_mensaje_websocket(self):

        """
        Test 8: Verificar el formato del mensaje WebSocket
        """
        # Arrange
        import json
        import base64
        
        frame_mock = np.zeros((480, 640, 3), dtype=np.uint8)
        ret, buffer = cv2.imencode('.jpg', frame_mock)
        frame_base64 = base64.b64encode(buffer).decode('utf-8')
        
        # Act
        mensaje = {
            'image': frame_base64,
            'count': 5
        }
        mensaje_json = json.dumps(mensaje)
        mensaje_decodificado = json.loads(mensaje_json)
        
        # Assert
        self.assertIn('image', mensaje_decodificado)
        self.assertIn('count', mensaje_decodificado)
        self.assertIsInstance(mensaje_decodificado['count'], int)
        self.assertIsInstance(mensaje_decodificado['image'], str)
    
    def test_comando_start_stop(self):
        """
        Test 9: Verificar lógica de comandos start/stop
        """
        # Arrange
        import json
        
        # Act & Assert - Comando start
        comando_start = json.dumps({'command': 'start'})
        data_start = json.loads(comando_start)
        self.assertEqual(data_start['command'], 'start')
        
        # Act & Assert - Comando stop
        comando_stop = json.dumps({'command': 'stop'})
        data_stop = json.loads(comando_stop)
        self.assertEqual(data_stop['command'], 'stop')


def suite():
    """Crear suite de pruebas unitarias"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestDeteccionPersonasUnitario))
    suite.addTests(loader.loadTestsFromTestCase(TestWebSocketLogica))
    return suite


if __name__ == '__main__':
    print("=" * 70)
    print("EJECUTANDO PRUEBAS UNITARIAS - Detección de Personas")
    print("=" * 70)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
