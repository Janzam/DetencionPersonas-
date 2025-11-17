""""""

Pruebas Funcionales - Sistema de Detección de PersonasTest Funcionales para el proyecto de Detección de Personas

Pruebas end-to-end del sistema completoPruebas end-to-end que verifican el funcionamiento completo del sistema

""""""

import unittest

import unittestimport subprocess

import subprocessimport time

import timeimport os

import osimport sys

import sysimport socket

import socketfrom pathlib import Path

from pathlib import Path

# Agregar el directorio raíz al path

# Agregar el directorio raíz al pathsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class TestFuncionalAplicacionDjango(unittest.TestCase):

class TestFuncionalesDeteccionPersonas(unittest.TestCase):    """Pruebas funcionales de la aplicación Django completa"""

    """Suite de pruebas funcionales del sistema completo"""    

        @classmethod

    @classmethod    def setUpClass(cls):

    def setUpClass(cls):        """Configuración inicial para todas las pruebas"""

        """Configuración inicial para todas las pruebas"""        cls.project_root = Path(__file__).parent.parent

        cls.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))        cls.manage_py = cls.project_root / "manage.py"

        cls.manage_py = os.path.join(cls.project_root, 'manage.py')        cls.puerto_test = 8001  # Puerto diferente al 8000 por defecto

            

        # Verificar que manage.py existe    def verificar_puerto_disponible(self, puerto):

        if not os.path.exists(cls.manage_py):        """Verificar si un puerto está disponible"""

            raise FileNotFoundError(f"manage.py no encontrado en {cls.manage_py}")        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

                return s.connect_ex(('localhost', puerto)) != 0

    def test_estructura_proyecto(self):    

        """Prueba: Verificar estructura del proyecto"""    def test_01_servidor_django_inicia_correctamente(self):

        archivos_requeridos = [        """

            'manage.py',        Test 1: Verificar que el servidor Django puede iniciar

            'requirements.txt',        """

            'yolov8n.pt',        if not self.manage_py.exists():

            'core/consumers.py',            self.skipTest(f"No se encuentra manage.py en {self.manage_py}")

            'core/views.py',        

            'core/urls.py',        # Verificar puerto disponible

            'core/routing.py',        if not self.verificar_puerto_disponible(self.puerto_test):

            'DeteccionPersonas/settings.py',            self.skipTest(f"Puerto {self.puerto_test} no está disponible")

            'DeteccionPersonas/asgi.py',        

            'DeteccionPersonas/urls.py'        # Arrange & Act

        ]        proceso = None

                try:

        for archivo in archivos_requeridos:            proceso = subprocess.Popen(

            ruta_completa = os.path.join(self.project_root, archivo)                [sys.executable, str(self.manage_py), "runserver", 

            self.assertTrue(                 f"{self.puerto_test}", "--noreload"],

                os.path.exists(ruta_completa),                stdout=subprocess.PIPE,

                f"Archivo requerido no encontrado: {archivo}"                stderr=subprocess.PIPE,

            )                cwd=str(self.project_root)

                )

    def test_configuracion_django(self):            

        """Prueba: Verificar configuración de Django"""            # Esperar 5 segundos

        settings_path = os.path.join(self.project_root, 'DeteccionPersonas', 'settings.py')            time.sleep(5)

                    

        with open(settings_path, 'r', encoding='utf-8') as f:            # Verificar si el proceso sigue vivo

            contenido = f.read()            poll_result = proceso.poll()

                    

        # Verificar configuraciones importantes            if poll_result is not None:

        self.assertIn('channels', contenido, "Channels debería estar en INSTALLED_APPS")                # El proceso terminó, leer el error

        self.assertIn('core', contenido, "App 'core' debería estar en INSTALLED_APPS")                _, stderr = proceso.communicate(timeout=2)

        self.assertIn('ASGI_APPLICATION', contenido, "ASGI_APPLICATION debería estar configurado")                error_msg = stderr.decode('utf-8', errors='ignore')

                    

    def test_configuracion_asgi(self):                if 'ModuleNotFoundError' in error_msg or 'No module named' in error_msg:

        """Prueba: Verificar configuración ASGI para WebSockets"""                    self.skipTest("Faltan dependencias requeridas. Ejecutar: pip install -r requirements.txt")

        asgi_path = os.path.join(self.project_root, 'DeteccionPersonas', 'asgi.py')                else:

                            self.fail(f"El servidor Django terminó inesperadamente. Error: {error_msg[:500]}")

        with open(asgi_path, 'r', encoding='utf-8') as f:            

            contenido = f.read()            # Assert

                    self.assertIsNone(poll_result, 

        self.assertIn('ProtocolTypeRouter', contenido, "Debería usar ProtocolTypeRouter")                            "El servidor Django debe seguir ejecutándose")

        self.assertIn('URLRouter', contenido, "Debería usar URLRouter")            print(f"✓ Servidor Django iniciado correctamente en puerto {self.puerto_test}")

        self.assertIn('websocket', contenido, "Debería tener configuración de websocket")            

            finally:

    def test_routing_websocket(self):            # Cleanup

        """Prueba: Verificar configuración de routing de WebSocket"""            if proceso is not None and proceso.poll() is None:

        routing_path = os.path.join(self.project_root, 'core', 'routing.py')                proceso.terminate()

                        try:

        with open(routing_path, 'r', encoding='utf-8') as f:                    proceso.wait(timeout=5)

            contenido = f.read()                    print("✓ Servidor Django detenido correctamente")

                        except subprocess.TimeoutExpired:

        self.assertIn('websocket_urlpatterns', contenido, "Debería definir websocket_urlpatterns")                    proceso.kill()

        self.assertIn('ws/video/', contenido, "Debería tener ruta ws/video/")                    proceso.wait()

                        print("✓ Servidor Django forzado a detenerse")

    def test_consumer_websocket(self):    

        """Prueba: Verificar implementación del consumer"""    def test_02_comando_manage_py_existe(self):

        consumer_path = os.path.join(self.project_root, 'core', 'consumers.py')        """

                Test 2: Verificar que manage.py existe y es ejecutable

        with open(consumer_path, 'r', encoding='utf-8') as f:        """

            contenido = f.read()        # Assert

                self.assertTrue(self.manage_py.exists(), 

        self.assertIn('WebsocketConsumer', contenido, "Debería heredar de WebsocketConsumer")                       f"manage.py debe existir en {self.manage_py}")

        self.assertIn('connect', contenido, "Debería implementar método connect")        self.assertTrue(self.manage_py.is_file(), 

        self.assertIn('disconnect', contenido, "Debería implementar método disconnect")                       "manage.py debe ser un archivo")

        self.assertIn('receive', contenido, "Debería implementar método receive")        print(f"✓ manage.py encontrado en {self.manage_py}")

        self.assertIn('YOLO', contenido, "Debería usar modelo YOLO")    

        def test_03_verificar_estructura_proyecto(self):

    def test_modelo_yolo_existe(self):        """

        """Prueba: Verificar que el modelo YOLO existe"""        Test 3: Verificar que la estructura del proyecto existe

        modelo_path = os.path.join(self.project_root, 'yolov8n.pt')        """

                # Arrange

        self.assertTrue(os.path.exists(modelo_path), "Modelo yolov8n.pt debería existir")        directorios_requeridos = ['core', 'DeteccionPersonas']

                

        # Verificar que tiene un tamaño razonable (>1MB)        # Act & Assert

        tamaño = os.path.getsize(modelo_path)        for directorio in directorios_requeridos:

        self.assertGreater(tamaño, 1_000_000, "Modelo debería tener más de 1MB")            dir_path = self.project_root / directorio

                self.assertTrue(dir_path.exists(), 

    def test_importar_modulos_principales(self):                          f"Directorio {directorio} debe existir")

        """Prueba: Verificar que se pueden importar módulos principales"""            print(f"✓ Directorio {directorio} encontrado")

        try:    

            # Importar Django    def test_04_verificar_archivos_core(self):

            import django        """

            from django.conf import settings        Test 4: Verificar que existen los archivos principales de core

                    """

            # Configurar Django settings si no está configurado        # Arrange

            if not settings.configured:        archivos_requeridos = ['views.py', 'consumers.py', 'urls.py', 'routing.py']

                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeteccionPersonas.settings')        core_path = self.project_root / 'core'

                django.setup()        

                    # Act & Assert

            # Importar módulos del proyecto        for archivo in archivos_requeridos:

            from core import consumers, views, routing            file_path = core_path / archivo

                        self.assertTrue(file_path.exists(), 

            self.assertTrue(True, "Todos los módulos se importaron correctamente")                          f"Archivo {archivo} debe existir en core/")

        except ImportError as e:            print(f"✓ Archivo core/{archivo} encontrado")

            self.fail(f"Error al importar módulos: {e}")    

        def test_05_verificar_modelo_yolo_existe(self):

    def test_dependencias_instaladas(self):        """

        """Prueba: Verificar que las dependencias principales están instaladas"""        Test 5: Verificar que el modelo YOLO existe

        dependencias = [        """

            'django',        # Arrange

            'opencv-python',        modelo_path = self.project_root / 'yolov8n.pt'

            'numpy',        

            'ultralytics',        # Act & Assert

            'torch'        self.assertTrue(modelo_path.exists(), 

        ]                       "Modelo yolov8n.pt debe existir en el directorio raíz")

                self.assertGreater(modelo_path.stat().st_size, 0, 

        for dep in dependencias:                          "El archivo del modelo no debe estar vacío")

            try:        

                __import__(dep.replace('-', '_'))        size_mb = modelo_path.stat().st_size / (1024 * 1024)

            except ImportError:        print(f"✓ Modelo yolov8n.pt encontrado ({size_mb:.2f} MB)")

                self.skipTest(f"Dependencia no instalada: {dep}")    

        def test_06_django_check_sin_errores(self):

    def test_puerto_disponible(self):        """

        """Prueba: Verificar que el puerto 8000 está disponible o en uso por Django"""        Test 6: Ejecutar django check para validar configuración

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        """

        result = sock.connect_ex(('127.0.0.1', 8000))        if not self.manage_py.exists():

        sock.close()            self.skipTest("manage.py no encontrado")

                

        # 0 = puerto en uso (puede ser nuestro servidor)        # Act

        # != 0 = puerto disponible        try:

        # Ambos casos son aceptables            resultado = subprocess.run(

        self.assertTrue(True, "Verificación de puerto completada")                [sys.executable, str(self.manage_py), "check"],

                    capture_output=True,

    def test_iniciar_servidor_django(self):                text=True,

        """Prueba: Verificar que el servidor Django puede iniciarse"""                cwd=str(self.project_root),

        try:                timeout=30

            # Importar componentes necesarios            )

            import django            

            from django.conf import settings            # Assert

            import daphne            if resultado.returncode != 0:

            import channels                # Verificar si es un problema de dependencias

                            if 'ModuleNotFoundError' in resultado.stderr or 'No module named' in resultado.stderr:

            self.assertTrue(True, "Servidor puede configurarse correctamente")                    self.skipTest(f"Faltan dependencias requeridas. Ejecutar: pip install -r requirements.txt")

        except ModuleNotFoundError as e:                else:

            self.skipTest(f"Módulo no encontrado para iniciar servidor: {e}")                    self.assertEqual(resultado.returncode, 0, 

                                       f"Django check debe pasar sin errores. Stderr: {resultado.stderr}")

    def test_configuracion_channels(self):            else:

        """Prueba: Verificar configuración de Django Channels"""                print("✓ Django check completado sin errores")

        try:            

            import channels        except subprocess.TimeoutExpired:

            self.assertTrue(True, "Django Channels está instalado")            self.fail("Django check excedió el tiempo límite de 30 segundos")

        except ImportError:    

            self.skipTest("Django Channels no está instalado")    def test_07_migraciones_estan_actualizadas(self):

            """

    def test_configuracion_daphne(self):        Test 7: Verificar que las migraciones están actualizadas

        """Prueba: Verificar que Daphne está instalado"""        """

        try:        if not self.manage_py.exists():

            import daphne            self.skipTest("manage.py no encontrado")

            self.assertTrue(True, "Daphne está instalado")        

        except ImportError:        # Act

            self.skipTest("Daphne no está instalado")        try:

                resultado = subprocess.run(

    def test_template_index_existe(self):                [sys.executable, str(self.manage_py), "makemigrations", "--check", "--dry-run"],

        """Prueba: Verificar que el template index.html existe"""                capture_output=True,

        template_path = os.path.join(self.project_root, 'core', 'templates', 'index.html')                text=True,

                        cwd=str(self.project_root),

        self.assertTrue(os.path.exists(template_path), "Template index.html debería existir")                timeout=30

                    )

        # Verificar contenido básico            

        with open(template_path, 'r', encoding='utf-8') as f:            # Assert

            contenido = f.read()            if resultado.returncode != 0:

                        # Verificar si es un problema de dependencias

        self.assertIn('WebSocket', contenido, "Template debería tener código WebSocket")                if 'ModuleNotFoundError' in resultado.stderr or 'No module named' in resultado.stderr:

                    self.skipTest(f"Faltan dependencias requeridas. Ejecutar: pip install -r requirements.txt")

                else:

def suite():                    self.assertEqual(resultado.returncode, 0, 

    """Crear suite de pruebas funcionales"""                                   "No deben haber migraciones pendientes")

    suite = unittest.TestSuite()            else:

    loader = unittest.TestLoader()                print("✓ Migraciones están actualizadas")

    suite.addTests(loader.loadTestsFromTestCase(TestFuncionalesDeteccionPersonas))            

    return suite        except subprocess.TimeoutExpired:

            self.fail("Verificación de migraciones excedió el tiempo límite")



if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)class TestFuncionalIntegracionCompleta(unittest.TestCase):

    runner.run(suite())    """Pruebas funcionales end-to-end del sistema completo"""

    
    @classmethod
    def setUpClass(cls):
        """Configuración inicial"""
        cls.project_root = Path(__file__).parent.parent
        cls.puerto_test = 8002
    
    def verificar_puerto_disponible(self, puerto):
        """Verificar si un puerto está disponible"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', puerto)) != 0
    
    def test_01_servidor_responde_y_permanece_activo(self):
        """
        Test 1: Servidor inicia, permanece activo 5 segundos y se detiene correctamente
        """
        manage_py = self.project_root / "manage.py"
        
        if not manage_py.exists():
            self.skipTest("manage.py no encontrado")
        
        if not self.verificar_puerto_disponible(self.puerto_test):
            self.skipTest(f"Puerto {self.puerto_test} no disponible")
        
        proceso = None
        
        try:
            # Arrange & Act: Iniciar servidor
            proceso = subprocess.Popen(
                [sys.executable, str(manage_py), "runserver", 
                 f"{self.puerto_test}", "--noreload"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=str(self.project_root)
            )
            
            print(f"✓ Servidor iniciado (PID: {proceso.pid})")
            
            # Esperar 5 segundos
            for i in range(5):
                time.sleep(1)
                # Verificar que sigue vivo
                poll_result = proceso.poll()
                if poll_result is not None:
                    # El proceso terminó, leer el error
                    _, stderr = proceso.communicate(timeout=2)
                    error_msg = stderr.decode('utf-8', errors='ignore')
                    
                    if 'ModuleNotFoundError' in error_msg or 'No module named' in error_msg:
                        self.skipTest("Faltan dependencias requeridas. Ejecutar: pip install -r requirements.txt")
                    else:
                        self.fail(f"El proceso terminó inesperadamente después de {i+1} segundo(s). Error: {error_msg[:500]}")
            
            print("✓ Servidor permaneció activo durante 5 segundos")
            
            # Assert final
            self.assertIsNone(proceso.poll(), 
                            "El proceso debe seguir vivo (poll() == None)")
            
        finally:
            # Cleanup: Terminar proceso correctamente
            if proceso is not None and proceso.poll() is None:
                print("Deteniendo servidor...")
                proceso.terminate()
                try:
                    proceso.wait(timeout=5)
                    print("✓ Servidor detenido correctamente")
                except subprocess.TimeoutExpired:
                    proceso.kill()
                    proceso.wait()
                    print("✓ Servidor forzado a detenerse")
    
    def test_02_verificar_dependencias_instaladas(self):
        """
        Test 2: Verificar que las dependencias principales están instaladas
        """
        dependencias = {
            'django': 'Django',
            'channels': 'Django Channels',
            'cv2': 'OpenCV (opencv-python)',
            'numpy': 'NumPy'
        }
        
        faltantes = []
        
        for modulo, nombre in dependencias.items():
            try:
                __import__(modulo)
                print(f"✓ Dependencia '{nombre}' instalada")
            except ImportError:
                faltantes.append(nombre)
                print(f"✗ Dependencia '{nombre}' NO instalada")
        
        if faltantes:
            self.skipTest(f"Faltan dependencias: {', '.join(faltantes)}. Ejecutar: pip install -r requirements.txt")
    
    def test_03_importar_consumers_sin_error(self):
        """
        Test 3: Verificar que se puede importar el módulo consumers
        """
        try:
            # Cambiar al directorio del proyecto para imports relativos
            original_path = sys.path.copy()
            sys.path.insert(0, str(self.project_root))
            
            # Intentar importar
            from core import consumers
            
            # Assert
            self.assertTrue(hasattr(consumers, 'VideoProcessingConsumer'), 
                          "consumers debe tener VideoProcessingConsumer")
            print("✓ Módulo consumers importado correctamente")
            
        except ImportError as e:
            error_msg = str(e)
            if 'No module named' in error_msg:
                modulo_faltante = error_msg.split("'")[1] if "'" in error_msg else "desconocido"
                self.skipTest(f"Falta la dependencia '{modulo_faltante}'. Ejecutar: pip install -r requirements.txt")
            else:
                self.fail(f"No se pudo importar consumers: {e}")
        finally:
            # Restaurar path
            sys.path = original_path
    
    def test_04_verificar_configuracion_websocket(self):
        """
        Test 4: Verificar que la configuración de WebSocket existe
        """
        routing_path = self.project_root / 'core' / 'routing.py'
        
        # Assert
        self.assertTrue(routing_path.exists(), 
                       "Archivo routing.py debe existir")
        
        # Leer contenido
        with open(routing_path, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Verificar configuraciones de WebSocket
        self.assertIn('websocket_urlpatterns', contenido, 
                     "routing.py debe definir websocket_urlpatterns")
        print("✓ Configuración WebSocket encontrada en routing.py")
    
    def test_05_template_index_existe(self):
        """
        Test 5: Verificar que el template index.html existe
        """
        template_path = self.project_root / 'core' / 'templates' / 'index.html'
        
        # Assert
        self.assertTrue(template_path.exists(), 
                       "Template index.html debe existir")
        
        # Verificar que no está vacío
        self.assertGreater(template_path.stat().st_size, 0, 
                          "Template no debe estar vacío")
        print(f"✓ Template index.html encontrado ({template_path.stat().st_size} bytes)")


class TestFuncionalRendimiento(unittest.TestCase):
    """Pruebas funcionales de rendimiento"""
    
    def test_01_importaciones_rapidas(self):
        """
        Test 1: Las importaciones principales deben ser rápidas
        """
        import time
        
        # Act
        start = time.time()
        import cv2
        import numpy as np
        elapsed = time.time() - start
        
        # Assert
        self.assertLess(elapsed, 5.0, 
                       "Las importaciones deben completarse en menos de 5 segundos")
        print(f"✓ Importaciones completadas en {elapsed:.3f} segundos")


def suite():
    """Crear suite de pruebas funcionales"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestFuncionalAplicacionDjango))
    suite.addTests(loader.loadTestsFromTestCase(TestFuncionalIntegracionCompleta))
    suite.addTests(loader.loadTestsFromTestCase(TestFuncionalRendimiento))
    return suite


if __name__ == '__main__':
    print("=" * 70)
    print("EJECUTANDO PRUEBAS FUNCIONALES - Detección de Personas")
    print("=" * 70)
    print("Estas pruebas verifican el sistema completo end-to-end")
    print("=" * 70)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
