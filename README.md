# Sistema de Detección de Personas en Tiempo Real

Sistema de visión por computadora para la detección y conteo de personas en tiempo real utilizando YOLOv8, Django y WebSockets.

## Tabla de Contenidos

### Documentación Técnica
1. [Descripción General](#descripción-general)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Ejecución](#ejecución)
6. [Pruebas](#pruebas)
7. [Tecnologías Utilizadas](#tecnologías-utilizadas)

### Documentación de Usuario
8. [Guía de Usuario](#documentación-de-usuario)
9. [Solución de Problemas](#solución-de-problemas)

---

# DOCUMENTACIÓN TÉCNICA

---

## Descripción General

Este proyecto implementa un sistema completo de detección de personas en tiempo real que:

- Captura video desde la cámara web del dispositivo
- Procesa cada frame utilizando el modelo YOLOv8 para detectar personas
- Transmite el video procesado y el conteo de personas al navegador mediante WebSockets
- Permite al usuario controlar el inicio y detención de la detección desde la interfaz web

### Características Principales

- **Detección en Tiempo Real**: Procesa video en tiempo real utilizando YOLOv8n (modelo nano optimizado para velocidad)
- **Comunicación Bidireccional**: WebSockets para transmisión de video y datos sin latencia
- **Interfaz Web Responsive**: Control intuitivo del sistema desde el navegador
- **Procesamiento Eficiente**: Optimizado para procesamiento en tiempo real con resizing de frames
- **Arquitectura Escalable**: Basado en Django Channels con servidor ASGI

---

## Requisitos del Sistema

### Requisitos de Hardware

- **Procesador**: Intel Core i5 o superior (recomendado i7 para mejor rendimiento)
- **RAM**: Mínimo 4GB (recomendado 8GB o más)
- **Cámara Web**: Cualquier cámara compatible con OpenCV
- **Almacenamiento**: Mínimo 500MB libres (para modelo YOLO y dependencias)

### Requisitos de Software

#### Python

- **Versión requerida**: Python 3.11
- **NO compatible**: Python 3.13 (debido a limitaciones de algunas dependencias)

#### Sistema Operativo

- Windows 10/11
- macOS 10.14 o superior
- Linux (Ubuntu 20.04 o superior, Debian, Fedora)

#### Navegadores Web Compatibles

- Google Chrome 90+
- Mozilla Firefox 88+
- Microsoft Edge 90+
- Safari 14+

### Dependencias Principales

| Dependencia | Versión | Propósito |
|------------|---------|-----------|
| Django | 5.2.7 | Framework web backend |
| channels | 4.3.1 | Soporte para WebSockets |
| daphne | 4.2.1 | Servidor ASGI |
| opencv-python | 4.10.0.84 | Procesamiento de video |
| ultralytics | 8.3.221 | Modelo YOLOv8 |
| numpy | >=1.23,<2.0 | Operaciones numéricas |
| torch | 2.5.1 | Framework de deep learning |

---

## Instalación

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/Janzam/DetencionPersonas-.git
cd DetencionPersonas-
```

### Paso 2: Verificar Versión de Python

```bash
python --version
```

Asegúrese de tener Python 3.11 instalado. Si tiene Python 3.13, consulte la sección de [Solución de Problemas](#solución-de-problemas).

### Paso 3: Crear Entorno Virtual con Python 3.11

#### En Windows (PowerShell)

```powershell
# Si tiene múltiples versiones de Python instaladas, especifique Python 3.11
py -3.11 -m venv venv
.\venv\Scripts\activate
```

#### En Windows (CMD)

```cmd
# Si tiene múltiples versiones de Python instaladas, especifique Python 3.11
py -3.11 -m venv venv
venv\Scripts\activate.bat
```

#### En Linux/macOS

```bash
# Asegúrese de usar Python 3.11
python3.11 -m venv venv
source venv/bin/activate
```

### Paso 4: Actualizar pip

```bash
python -m pip install --upgrade pip
```

### Paso 5: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Este proceso puede tardar varios minutos ya que descargará e instalará todas las dependencias necesarias, incluyendo PyTorch y el modelo YOLO.

### Paso 6: Aplicar Migraciones de Base de Datos

```bash
python manage.py migrate
```

### Paso 7: Verificar Instalación

Ejecute el script de verificación para confirmar que todo está configurado correctamente:

```bash
python verificar_entorno.py
```

Este script verificará:
- Versión de Python
- Dependencias instaladas
- Estructura del proyecto
- Modelo YOLO
- Configuración de Django
- Puertos disponibles

---

## Estructura del Proyecto

```
DetencionPersonas-/
│
├── manage.py                      # Script de gestión de Django
├── requirements.txt               # Dependencias del proyecto
├── yolov8n.pt                    # Modelo YOLOv8 nano
├── db.sqlite3                    # Base de datos SQLite
│
├── core/                         # Aplicación principal
│   ├── __init__.py
│   ├── admin.py                  # Configuración del admin de Django
│   ├── apps.py                   # Configuración de la aplicación
│   ├── consumers.py              # Consumer de WebSocket para video
│   ├── models.py                 # Modelos de base de datos
│   ├── routing.py                # Rutas de WebSocket
│   ├── urls.py                   # URLs de la aplicación
│   ├── views.py                  # Vistas de Django
│   └── templates/
│       └── index.html            # Interfaz web principal
│
├── DeteccionPersonas/            # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py                   # Configuración ASGI
│   ├── settings.py               # Configuración de Django
│   ├── urls.py                   # URLs principales
│   └── wsgi.py                   # Configuración WSGI
│
├── tests/                        # Suite de pruebas
│   ├── __init__.py
│   ├── test_unitarios.py         # Pruebas unitarias
│   ├── test_integracion.py       # Pruebas de integración
│   ├── test_funcionales.py       # Pruebas funcionales
│   ├── run_all_tests.py          # Ejecutor de todas las pruebas
│   ├── crear_imagen_prueba.py    # Generador de imágenes de prueba
│   ├── README.md                 # Documentación de pruebas
│   └── imagenes/                 # Imágenes para pruebas
│       └── prueba1.jpg
│
└── 
```

### Descripción de Componentes Principales

#### core/consumers.py
Implementa el WebSocket consumer que:
- Gestiona conexiones WebSocket
- Captura video desde la cámara
- Procesa frames con YOLOv8
- Envía video procesado y conteo al cliente

#### core/views.py
Define las vistas HTTP:
- Vista principal que renderiza index.html

#### core/routing.py
Configura las rutas de WebSocket:
- Define el patrón de URL para la conexión WebSocket

#### DeteccionPersonas/asgi.py
Configuración ASGI que integra:
- Manejo de HTTP tradicional
- Manejo de WebSocket
- Middleware de autenticación

---

## Ejecución

### Iniciar el Servidor

Una vez completada la instalación, inicie el servidor de desarrollo:

```bash
python manage.py runserver
```

El servidor iniciará en `http://127.0.0.1:8000/` por defecto.

### Usar un Puerto Diferente

```bash
python manage.py runserver 8080
```

### Permitir Acceso Desde Otras Máquinas en la Red

```bash
python manage.py runserver 0.0.0.0:8000
```

### Verificar que el Servidor Está Funcionando

Abra un navegador y navegue a:
```
http://127.0.0.1:8000/
```

Debería ver la interfaz del sistema de detección de personas.

### Detener el Servidor

Presione `Ctrl + C` en la terminal donde está ejecutándose el servidor.

---

# DOCUMENTACIÓN DE USUARIO

---

## Documentación de Usuario

### Acceso al Sistema

1. Asegúrese de que el servidor esté en ejecución
2. Abra un navegador web compatible
3. Navegue a `http://127.0.0.1:8000/`

### Uso del Sistema

#### Iniciar Detección

1. En la página principal, localice el botón "Iniciar Detección"
2. Haga clic en el botón
3. El navegador solicitará permiso para acceder a la cámara web
4. Conceda los permisos necesarios
5. El sistema comenzará a:
   - Capturar video desde su cámara
   - Detectar personas en cada frame
   - Mostrar el video procesado con rectángulos verdes alrededor de las personas detectadas
   - Mostrar el conteo de personas en tiempo real en la esquina superior izquierda

#### Detener Detección

1. Haga clic en el botón "Detener Detección"
2. El procesamiento de video se detendrá
3. La cámara será liberada

#### Reiniciar Detección

Puede iniciar y detener la detección cuantas veces sea necesario sin recargar la página.

### Interpretación de Resultados

#### Visualización del Video

- **Rectángulos Verdes**: Indican personas detectadas
- **Texto Superior Izquierdo**: Muestra "Personas: N" donde N es el conteo actual
- **Rectángulos en Movimiento**: Siguen a las personas mientras se mueven

#### Conteo de Personas

- El conteo se actualiza en tiempo real (aproximadamente 20 veces por segundo)
- Solo se cuentan objetos clasificados como "persona" (clase 0 del dataset COCO)
- El conteo incluye personas parcialmente visibles
- El sistema puede detectar múltiples personas simultáneamente

#### Rendimiento Esperado

- **Latencia**: Típicamente < 100ms entre captura y visualización
- **Precisión**: Depende de las condiciones de iluminación y distancia
- **FPS**: Aproximadamente 15-20 frames por segundo en hardware moderno

### Consideraciones de Uso

#### Mejores Prácticas

1. **Iluminación**: Asegure buena iluminación para mejor precisión
2. **Distancia**: Las personas deben estar claramente visibles en el frame
3. **Ángulo**: Posicione la cámara para capturar personas frontalmente
4. **Fondo**: Fondos simples mejoran la detección

#### Limitaciones

1. **Oclusión**: Personas parcialmente ocultas pueden no detectarse
2. **Distancia**: Personas muy lejanas pueden no detectarse
3. **Ángulos Extremos**: Vistas desde arriba o abajo reducen precisión
4. **Velocidad**: Movimientos muy rápidos pueden causar detecciones intermitentes

---

## Pruebas

El proyecto incluye una suite completa de pruebas organizadas en tres niveles:

### Suite de Pruebas

| Tipo | Archivo | Cantidad | Duración |
|------|---------|----------|----------|
| Unitarias | test_unitarios.py | 9 | ~2 segundos |
| Integración | test_integracion.py | 13 | ~30 segundos |
| Funcionales | test_funcionales.py | 13 | ~20 segundos |

### Ejecutar Todas las Pruebas

```bash
python tests/run_all_tests.py
```

### Ejecutar Pruebas Específicas

#### Solo Pruebas Unitarias
```bash
python tests/test_unitarios.py
```

#### Solo Pruebas de Integración
```bash
python tests/test_integracion.py
```

#### Solo Pruebas Funcionales
```bash
python tests/test_funcionales.py
```

### Ejecutar con unittest

```bash
# Descubrir y ejecutar todas las pruebas
python -m unittest discover -s tests -v

# Ejecutar prueba específica
python -m unittest tests.test_unitarios.TestDeteccionPersonasUnitario.test_procesar_frame_sin_personas -v
```

### Ejecutar con pytest (opcional)

```bash
# Instalar pytest
pip install pytest pytest-cov

# Ejecutar todas las pruebas
pytest tests/ -v

# Con cobertura de código
pytest tests/ -v --cov=core --cov-report=html
```

### Cobertura de Código

```bash
# Instalar coverage
pip install coverage

# Ejecutar pruebas con cobertura
coverage run -m unittest discover -s tests

# Ver reporte
coverage report

# Generar HTML
coverage html
# Abrir htmlcov/index.html
```

### Preparación de Pruebas

Antes de ejecutar pruebas de integración, cree una imagen de prueba:

```bash
python tests/crear_imagen_prueba.py
```

### Pruebas Realizadas

#### Pruebas Unitarias
- Procesamiento de frames sin personas
- Procesamiento de frames con múltiples personas
- Estructura de datos de retorno
- Filtrado de clases de objetos
- Validación de coordenadas
- Manejo de errores
- Formato de mensajes WebSocket
- Comandos de control

#### Pruebas de Integración
- Carga del modelo YOLO
- Procesamiento de imágenes reales
- Detección en imágenes de prueba
- Codificación de frames a base64
- Rendimiento del procesamiento
- Integración OpenCV-YOLO

#### Pruebas Funcionales
- Inicio del servidor Django
- Verificación de estructura del proyecto
- Validación de configuración
- Importación de módulos
- Verificación de dependencias
- Configuración de WebSocket

### Documentación Adicional de Pruebas

Para documentación detallada sobre las pruebas, consulte:
- `tests/README.md` - Guía de pruebas
- `TESTING.md` - Documentación completa de testing

---

## Tecnologías Utilizadas

### Backend

**Django 5.2.7**
- Framework web principal
- Manejo de rutas HTTP
- ORM para base de datos
- Sistema de templates

**Django Channels 4.3.1**
- Soporte para WebSockets
- Comunicación asíncrona
- Manejo de eventos en tiempo real

**Daphne 4.2.1**
- Servidor ASGI
- Manejo de protocolos HTTP y WebSocket
- Soporte para aplicaciones asíncronas

### Visión por Computadora

**YOLOv8 (Ultralytics 8.3.221)**
- Modelo de detección de objetos
- Versión nano (yolov8n.pt) para velocidad
- Detección en tiempo real
- Pre-entrenado en dataset COCO

**OpenCV 4.10.0.84**
- Captura de video desde cámara
- Procesamiento de imágenes
- Redimensionamiento de frames
- Codificación de imágenes

**PyTorch 2.5.1**
- Framework de deep learning
- Backend para YOLOv8
- Procesamiento en GPU (opcional)

### Frontend

**HTML5**
- Estructura de la interfaz
- WebSocket API
- Canvas para video

**CSS3**
- Estilos de la interfaz
- Diseño responsive
- Animaciones

**JavaScript**
- Lógica de cliente
- Manejo de WebSocket
- Decodificación de imágenes base64
- Control de eventos

### Librerías Auxiliares

**NumPy >=1.23,<2.0**
- Operaciones con arrays
- Procesamiento numérico
- Manipulación de imágenes

**Base64**
- Codificación de frames
- Transmisión de imágenes por WebSocket

---

## Solución de Problemas

### Problema: Python 3.13 Incompatible

**Síntoma**: Error al instalar dependencias o ejecutar pruebas

**Solución**:
```powershell
# Usar Python 3.11 específicamente
py -3.11 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

**Razón**: Algunas dependencias no soportan Python 3.13. Se recomienda usar Python 3.11

### Problema: Error "No module named 'channels'"

**Síntoma**: Error al iniciar el servidor

**Solución**:
```bash
pip install -r requirements.txt
```

**Verificar**:
```bash
python -c "import channels; print('Channels instalado correctamente')"
```

### Problema: Error "No module named 'daphne'"

**Síntoma**: El servidor no inicia

**Solución**:
```bash
pip install daphne
```

### Problema: La Cámara No Se Detecta

**Síntomas**: Video negro o error al iniciar detección

**Soluciones**:

1. Verificar permisos de cámara en el navegador
2. Verificar que la cámara funcione:
   ```python
   import cv2
   cap = cv2.VideoCapture(0)
   print(cap.isOpened())
   ```
3. Cerrar otras aplicaciones que usen la cámara
4. Reiniciar el navegador

### Problema: Modelo YOLO No Se Descarga

**Síntoma**: Error al importar ultralytics

**Solución**:
```bash
# Descargar manualmente
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

El modelo se descargará automáticamente (~6MB).

### Problema: Puerto 8000 en Uso

**Síntoma**: Error "Address already in use"

**Solución en Windows**:
```powershell
# Encontrar proceso
netstat -ano | findstr :8000
# Terminar proceso (reemplazar PID)
taskkill /PID <PID> /F
```

**Solución en Linux/macOS**:
```bash
# Encontrar y terminar proceso
lsof -ti:8000 | xargs kill -9
```

**Alternativa**:
```bash
# Usar otro puerto
python manage.py runserver 8080
```

### Problema: Latencia Alta

**Síntomas**: Video con retraso, FPS bajo

**Soluciones**:

1. Reducir resolución en consumers.py:
   ```python
   frame_resized = cv2.resize(frame, (320, 240))
   ```

2. Aumentar intervalo de sleep:
   ```python
   time.sleep(0.1)  # En lugar de 0.05
   ```

3. Cerrar aplicaciones que consuman CPU/GPU

### Problema: Detección Inexacta

**Síntomas**: No detecta personas o detecta objetos incorrectos

**Soluciones**:

1. Mejorar iluminación
2. Acercar personas a la cámara
3. Usar modelo más grande (yolov8s.pt, yolov8m.pt)
4. Ajustar threshold de confianza en consumers.py

### Problema: Error en Migraciones

**Síntoma**: Error al ejecutar `migrate`

**Solución**:
```bash
# Eliminar base de datos y recrear
rm db.sqlite3
python manage.py migrate
```

### Problema: WebSocket No Conecta

**Síntomas**: Video no se muestra, sin mensajes de error

**Verificaciones**:

1. Verificar routing.py existe y está configurado
2. Verificar asgi.py incluye WebSocket routing
3. Verificar navegador soporta WebSocket
4. Ver consola del navegador (F12) para errores

**Solución**:
```bash
# Reiniciar servidor
Ctrl+C
python manage.py runserver
```

### Obtener Ayuda Adicional

Si los problemas persisten:

1. Ejecute el script de verificación:
   ```bash
   python verificar_entorno.py
   ```

2. Revise los logs del servidor

3. Consulte la documentación adicional:
   - `TESTING.md`
   - `PYTHON_3.13_NOTES.md`
   - `DEPENDENCIAS_FALTANTES.md`


### Repositorio

```
https://github.com/Janzam/DetencionPersonas-.git
```
