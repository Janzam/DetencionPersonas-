""""""

Pruebas de Integración - Sistema de Detección de PersonasTest de Integración para el proyecto de Detección de Personas

Pruebas con componentes reales (YOLO, OpenCV)Pruebas que integran componentes reales: modelo YOLO real, procesamiento real de imágenes

""""""

import unittest

import unittestimport os

import osimport sys

import sysimport cv2

import cv2import numpy as np

import numpy as np

import base64# Agregar el directorio raíz al path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agregar el directorio raíz al path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))# Importar después de agregar al path

try:

    from ultralytics import YOLO

class TestIntegracionDeteccionPersonas(unittest.TestCase):    YOLO_DISPONIBLE = True

    """Suite de pruebas de integración"""except ImportError:

        YOLO_DISPONIBLE = False

    @classmethod    print("WARNING: ultralytics no está instalado. Algunas pruebas se saltarán.")

    def setUpClass(cls):

        """Configuración una vez para todas las pruebas"""

        try:class TestIntegracionYOLO(unittest.TestCase):

            from ultralytics import YOLO    """Pruebas de integración con el modelo YOLO real"""

            cls.modelo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'yolov8n.pt')    

                @classmethod

            if not os.path.exists(cls.modelo_path):    def setUpClass(cls):

                cls.skipTest(cls, f"Modelo YOLO no encontrado en {cls.modelo_path}")        """Configuración una vez para todas las pruebas de la clase"""

                    cls.model_path = 'yolov8n.pt'

            cls.modelo = YOLO(cls.modelo_path)        cls.imagen_test_path = os.path.join(

        except Exception as e:            os.path.dirname(__file__), 

            cls.skipTest(cls, f"No se pudo cargar YOLO: {e}")            'imagenes', 

                'prueba1.jpg'

    def setUp(self):        )

        """Configuración para cada prueba"""        

        # Crear frame de prueba        # Verificar que existe el modelo

        self.frame_prueba = np.zeros((480, 640, 3), dtype=np.uint8)        if not os.path.exists(cls.model_path):

                    print(f"WARNING: No se encuentra el modelo en {cls.model_path}")

        # Path para imágenes de prueba    

        self.tests_dir = os.path.dirname(__file__)    @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")

        self.imagenes_dir = os.path.join(self.tests_dir, 'imagenes')    def test_01_cargar_modelo_yolo(self):

            """

    def test_cargar_modelo_yolo(self):        Test 1: Verificar que el modelo YOLO carga correctamente

        """Prueba: Cargar modelo YOLO correctamente"""        """

        self.assertIsNotNone(self.modelo, "Modelo YOLO debería cargarse correctamente")        # Act

        self.assertTrue(hasattr(self.modelo, '__call__'), "Modelo debería ser callable")        try:

                model = YOLO(self.model_path)

    def test_procesar_frame_con_modelo_real(self):            # Assert

        """Prueba: Procesar frame con modelo YOLO real"""            self.assertIsNotNone(model, "El modelo debe cargarse correctamente")

        results = self.modelo(self.frame_prueba)            print(f"✓ Modelo cargado desde: {self.model_path}")

                except Exception as e:

        self.assertIsNotNone(results, "Resultados no deberían ser None")            self.fail(f"Error al cargar el modelo YOLO: {e}")

        self.assertIsInstance(results, list, "Resultados deberían ser una lista")    

        @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")

    def test_deteccion_en_imagen_vacia(self):    def test_02_modelo_acepta_frame_numpy(self):

        """Prueba: Detección en imagen vacía (sin personas)"""        """

        results = self.modelo(self.frame_prueba)        Test 2: Verificar que el modelo acepta frames de tipo numpy array

                """

        # Contar personas detectadas        # Arrange

        conteo = 0        model = YOLO(self.model_path)

        for result in results:        frame_test = np.zeros((480, 640, 3), dtype=np.uint8)

            for box in result.boxes:        

                if int(box.cls[0]) == 0:  # Clase 0 = persona        # Act & Assert

                    conteo += 1        try:

                    results = model(frame_test, verbose=False)

        # En una imagen negra, no debería detectar personas            self.assertIsNotNone(results, "El modelo debe retornar resultados")

        self.assertEqual(conteo, 0, "No debería detectar personas en imagen vacía")            print("✓ Modelo acepta frames numpy correctamente")

            except Exception as e:

    def test_deteccion_en_imagen_prueba(self):            self.fail(f"Error al procesar frame numpy: {e}")

        """Prueba: Detección en imagen de prueba con persona dibujada"""    

        # Crear imagen con figura humanoide simple    @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")

        frame = np.zeros((480, 640, 3), dtype=np.uint8)    def test_03_procesar_imagen_real(self):

                """

        # Dibujar forma humana simple (rectángulos)        Test 3: Procesar una imagen real y validar resultados

        cv2.rectangle(frame, (250, 100), (390, 400), (255, 255, 255), -1)  # Cuerpo        """

        cv2.circle(frame, (320, 60), 30, (255, 255, 255), -1)  # Cabeza        # Verificar si existe imagen de prueba

                if not os.path.exists(self.imagen_test_path):

        results = self.modelo(frame)            self.skipTest(f"No se encuentra imagen de prueba en {self.imagen_test_path}")

                

        self.assertIsNotNone(results, "Resultados no deberían ser None")        # Arrange

        self.assertTrue(len(results) > 0, "Debería haber al menos un resultado")        model = YOLO(self.model_path)

            frame = cv2.imread(self.imagen_test_path)

    def test_estructura_resultado_yolo(self):        

        """Prueba: Verificar estructura del resultado de YOLO"""        self.assertIsNotNone(frame, f"No se pudo cargar la imagen {self.imagen_test_path}")

        results = self.modelo(self.frame_prueba)        

                # Act

        self.assertTrue(hasattr(results[0], 'boxes'), "Resultado debería tener atributo 'boxes'")        results = model(frame, verbose=False)

                

        # Verificar que boxes es iterable        # Assert

        try:        self.assertIsNotNone(results, "Debe retornar resultados")

            for box in results[0].boxes:        self.assertGreater(len(results), 0, "Debe haber al menos un resultado")

                pass        print(f"✓ Imagen procesada correctamente: {self.imagen_test_path}")

        except TypeError:    

            self.fail("boxes debería ser iterable")    @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")

        def test_04_detectar_personas_retorna_entero(self):

    def test_codificar_frame_a_base64(self):        """

        """Prueba: Codificar frame a base64 para WebSocket"""        Test 4: Verificar que el conteo de personas retorna un entero

        # Codificar frame        """

        _, buffer = cv2.imencode('.jpg', self.frame_prueba)        # Arrange

        frame_base64 = base64.b64encode(buffer).decode('utf-8')        model = YOLO(self.model_path)

                frame_test = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

        self.assertIsInstance(frame_base64, str, "Frame codificado debería ser string")        

        self.assertTrue(len(frame_base64) > 0, "Frame codificado no debería estar vacío")        # Act

            results = model(frame_test, classes=0, verbose=False)  # Clase 0 = persona

    def test_decodificar_frame_desde_base64(self):        person_count = 0

        """Prueba: Decodificar frame desde base64"""        

        # Codificar        for r in results:

        _, buffer = cv2.imencode('.jpg', self.frame_prueba)            person_count = len(r.boxes)

        frame_base64 = base64.b64encode(buffer).decode('utf-8')        

                # Assert

        # Decodificar        self.assertIsInstance(person_count, int, "El conteo debe ser un entero")

        frame_bytes = base64.b64decode(frame_base64)        self.assertGreaterEqual(person_count, 0, "El conteo no debe ser negativo")

        frame_array = np.frombuffer(frame_bytes, dtype=np.uint8)        print(f"✓ Conteo de personas: {person_count} (tipo: {type(person_count).__name__})")

        frame_decodificado = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)    

            @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")

        self.assertIsNotNone(frame_decodificado, "Frame decodificado no debería ser None")    def test_05_detectar_minimo_una_persona_en_imagen_real(self):

        self.assertEqual(frame_decodificado.shape, self.frame_prueba.shape, "Dimensiones deberían coincidir")        """

            Test 5: Verificar que se detecta al menos una persona en imagen de prueba

    def test_redimensionar_frame(self):        """

        """Prueba: Redimensionar frame para procesamiento"""        if not os.path.exists(self.imagen_test_path):

        nuevo_ancho = 320            self.skipTest(f"No se encuentra imagen de prueba en {self.imagen_test_path}")

        nuevo_alto = 240        

                # Arrange

        frame_redimensionado = cv2.resize(self.frame_prueba, (nuevo_ancho, nuevo_alto))        model = YOLO(self.model_path)

                frame = cv2.imread(self.imagen_test_path)

        self.assertEqual(frame_redimensionado.shape[1], nuevo_ancho, "Ancho debería ser 320")        

        self.assertEqual(frame_redimensionado.shape[0], nuevo_alto, "Alto debería ser 240")        # Act

            results = model(frame, classes=0, verbose=False)

    def test_dibujar_bounding_box(self):        person_count = 0

        """Prueba: Dibujar bounding box en frame"""        

        frame_copia = self.frame_prueba.copy()        for r in results:

                    person_count = len(r.boxes)

        # Dibujar rectángulo        

        cv2.rectangle(frame_copia, (100, 100), (200, 300), (0, 255, 0), 2)        # Assert

                self.assertGreaterEqual(person_count, 1, 

        # Verificar que el frame fue modificado                               "Debe detectar al menos 1 persona en la imagen de prueba")

        diferencia = cv2.subtract(frame_copia, self.frame_prueba)        print(f"✓ Personas detectadas en imagen real: {person_count}")

        self.assertTrue(diferencia.any(), "Frame debería haber sido modificado")    

        @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")

    def test_agregar_texto_contador(self):    def test_06_cajas_es_lista(self):

        """Prueba: Agregar texto de contador al frame"""        """

        frame_copia = self.frame_prueba.copy()        Test 6: Verificar que 'cajas' es una lista

                """

        # Agregar texto        # Arrange

        texto = "Personas: 3"        model = YOLO(self.model_path)

        cv2.putText(frame_copia, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)        frame_test = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

                

        # Verificar que el frame fue modificado        # Act

        diferencia = cv2.subtract(frame_copia, self.frame_prueba)        results = model(frame_test, classes=0, verbose=False)

        self.assertTrue(diferencia.any(), "Frame debería tener texto agregado")        cajas = []

            

    def test_performance_deteccion(self):        for r in results:

        """Prueba: Medir tiempo de detección"""            for box in r.boxes.xyxy:

        import time                x1, y1, x2, y2 = map(int, box.tolist())

                        cajas.append((x1, y1, x2, y2))

        inicio = time.time()        

        results = self.modelo(self.frame_prueba)        # Assert

        fin = time.time()        self.assertIsInstance(cajas, list, "'cajas' debe ser una lista")

                print(f"✓ Tipo de 'cajas': {type(cajas).__name__} con {len(cajas)} elementos")

        tiempo_procesamiento = fin - inicio    

            @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")

        # En un sistema moderno, debería procesar en menos de 1 segundo    def test_07_coordenadas_cajas_son_tuplas(self):

        self.assertLess(tiempo_procesamiento, 1.0, "Detección debería ser rápida (<1s)")        """

            Test 7: Verificar que cada caja contiene tuplas de 4 coordenadas

    def test_multiples_detecciones_consecutivas(self):        """

        """Prueba: Procesar múltiples frames consecutivamente"""        # Arrange

        num_frames = 5        model = YOLO(self.model_path)

                # Crear imagen con algo de contenido

        for i in range(num_frames):        frame_test = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

            results = self.modelo(self.frame_prueba)        

            self.assertIsNotNone(results, f"Frame {i+1} debería procesarse correctamente")        # Act

        results = model(frame_test, classes=0, verbose=False)

        cajas = []

def suite():        

    """Crear suite de pruebas de integración"""        for r in results:

    suite = unittest.TestSuite()            for box in r.boxes.xyxy:

    loader = unittest.TestLoader()                x1, y1, x2, y2 = map(int, box.tolist())

    suite.addTests(loader.loadTestsFromTestCase(TestIntegracionDeteccionPersonas))                cajas.append((x1, y1, x2, y2))

    return suite        

        # Assert

        for caja in cajas:

if __name__ == '__main__':            self.assertIsInstance(caja, tuple, "Cada caja debe ser una tupla")

    runner = unittest.TextTestRunner(verbosity=2)            self.assertEqual(len(caja), 4, "Cada caja debe tener 4 coordenadas")

    runner.run(suite())            # Verificar que son enteros

            for coord in caja:
                self.assertIsInstance(coord, int, "Las coordenadas deben ser enteros")
        
        print(f"✓ {len(cajas)} cajas validadas correctamente")
    
    @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")
    def test_08_integracion_completa_procesar_frame(self):
        """
        Test 8: Prueba de integración completa del flujo de procesamiento
        """
        # Arrange
        model = YOLO(self.model_path)
        frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        
        # Act - Simular el flujo completo del consumer
        frame_resized = cv2.resize(frame, (640, 480))
        results = model(frame_resized, classes=0, verbose=False)
        
        person_count = 0
        cajas = []
        
        for r in results:
            person_count = len(r.boxes)
            for box in r.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box.tolist())
                cajas.append((x1, y1, x2, y2))
                # Dibujar rectángulo (como en el código real)
                cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Añadir texto (como en el código real)
        cv2.putText(frame_resized, f'Personas: {person_count}', 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        # Assert
        self.assertIsNotNone(frame_resized, "Frame procesado no debe ser None")
        self.assertEqual(frame_resized.shape, (480, 640, 3), 
                        "Dimensiones del frame deben ser correctas")
        self.assertIsInstance(person_count, int, "Conteo debe ser entero")
        self.assertIsInstance(cajas, list, "Cajas debe ser lista")
        
        print(f"✓ Integración completa exitosa - Personas: {person_count}, Cajas: {len(cajas)}")
    
    @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")
    def test_09_codificar_frame_a_base64(self):
        """
        Test 9: Verificar codificación de frame a base64 (para WebSocket)
        """
        import base64
        
        # Arrange
        frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        
        # Act
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_base64 = base64.b64encode(buffer).decode('utf-8')
        
        # Assert
        self.assertTrue(ret, "La codificación debe ser exitosa")
        self.assertIsInstance(frame_base64, str, "Base64 debe ser string")
        self.assertGreater(len(frame_base64), 0, "Base64 no debe estar vacío")
        
        print(f"✓ Frame codificado a base64 ({len(frame_base64)} caracteres)")
    
    @unittest.skipUnless(YOLO_DISPONIBLE, "Requiere ultralytics instalado")
    def test_10_rendimiento_procesamiento(self):
        """
        Test 10: Verificar que el procesamiento se completa en tiempo razonable
        """
        import time
        
        # Arrange
        model = YOLO(self.model_path)
        frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        
        # Act
        start_time = time.time()
        results = model(frame, classes=0, verbose=False)
        person_count = len(results[0].boxes)
        elapsed_time = time.time() - start_time
        
        # Assert
        self.assertLess(elapsed_time, 2.0, 
                       "El procesamiento debe completarse en menos de 2 segundos")
        
        print(f"✓ Procesamiento completado en {elapsed_time:.3f} segundos")


class TestIntegracionOpenCV(unittest.TestCase):
    """Pruebas de integración con OpenCV"""
    
    def test_crear_imagen_sintetica(self):
        """
        Test 11: Verificar creación de imágenes sintéticas con OpenCV
        """
        # Act
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Assert
        self.assertEqual(frame.shape, (480, 640, 3))
        self.assertEqual(frame.dtype, np.uint8)
        print(f"✓ Imagen sintética creada: {frame.shape}")
    
    def test_resize_frame(self):
        """
        Test 12: Verificar redimensionamiento de frames
        """
        # Arrange
        frame = np.random.randint(0, 255, (720, 1280, 3), dtype=np.uint8)
        
        # Act
        frame_resized = cv2.resize(frame, (640, 480))
        
        # Assert
        self.assertEqual(frame_resized.shape, (480, 640, 3))
        print(f"✓ Frame redimensionado de {frame.shape} a {frame_resized.shape}")
    
    def test_dibujar_rectangulo_no_modifica_dimensiones(self):
        """
        Test 13: Verificar que dibujar rectángulos no cambia dimensiones
        """
        # Arrange
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        original_shape = frame.shape
        
        # Act
        cv2.rectangle(frame, (100, 100), (200, 200), (0, 255, 0), 2)
        
        # Assert
        self.assertEqual(frame.shape, original_shape)
        print("✓ Dimensiones preservadas después de dibujar rectángulo")


def suite():
    """Crear suite de pruebas de integración"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestIntegracionYOLO))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegracionOpenCV))
    return suite


if __name__ == '__main__':
    print("=" * 70)
    print("EJECUTANDO PRUEBAS DE INTEGRACIÓN - Detección de Personas")
    print("=" * 70)
    print("Estas pruebas usan el modelo YOLO real y OpenCV")
    print("=" * 70)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
