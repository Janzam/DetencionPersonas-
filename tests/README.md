# Documentación de Pruebas - Sistema de Detección de Personas# Guía de Pruebas - Proyecto Detección de Personas



## Descripción## Descripción



Este directorio contiene la suite completa de pruebas para el sistema de detección de personas en tiempo real. Las pruebas están organizadas en tres niveles siguiendo las mejores prácticas de testing.Este proyecto incluye una suite completa de pruebas para validar el sistema de detección de personas usando YOLOv8 y Django WebSockets.



## Estructura de Pruebas## Estructura de Pruebas



``````

tests/tests/

├── __init__.py                 # Inicialización del paquete├── __init__.py                 # Inicialización del paquete

├── test_unitarios.py          # Pruebas unitarias (9 tests)├── test_unitarios.py          # Pruebas unitarias (sin dependencias)

├── test_integracion.py        # Pruebas de integración (13 tests)├── test_integracion.py        # Pruebas de integración (con YOLO real)

├── test_funcionales.py        # Pruebas funcionales (13 tests)├── test_funcionales.py        # Pruebas funcionales (end-to-end)

├── run_all_tests.py           # Ejecutor de todas las pruebas├── run_all_tests.py           # Script para ejecutar todas las pruebas

├── crear_imagen_prueba.py     # Generador de imágenes de prueba└── imagenes/                  # Imágenes para pruebas

├── README.md                  # Esta documentación    └── prueba1.jpg           # Imagen de prueba (debe contener personas)

└── imagenes/                  # Imágenes para testing```

    └── prueba1.jpg

```## Tipos de Pruebas



## Tipos de Pruebas### 1. Pruebas Unitarias (`test_unitarios.py`)

**Objetivo:** Probar componentes aislados sin dependencias externas.

### Pruebas Unitarias (test_unitarios.py)

**Características:**

Prueban componentes individuales de forma aislada usando mocks.- No usa modelo YOLO real

- No requiere cámara

**Características:**- Usa mocks y simulaciones

- No requieren dependencias externas- Ejecución rápida

- Rápidas de ejecutar (~2 segundos)

- Usan mocks para simular modelo YOLO**Ejecutar:**

- Verifican lógica de negocio```bash

python tests/test_unitarios.py

**Tests incluidos:**```

- Procesamiento de frames sin personas

- Procesamiento con una persona**Pruebas incluidas:**

- Procesamiento con múltiples personas- Procesar frame sin personas retorna 0

- Filtrado de clases de objetos- Procesar frame con 2 personas retorna 2

- Validación de coordenadas- Retorna diccionario con claves "count" y "cajas"

- Niveles de confianza- Filtrar solo objetos de clase 0 (personas)

- Formato de mensajes WebSocket- Validar coordenadas de cajas

- Comandos de control- Formato de mensajes WebSocket

- Comandos start/stop

**Ejecutar:**

```bash### 2. Pruebas de Integración (`test_integracion.py`)

python tests/test_unitarios.py**Objetivo:** Probar la integración entre componentes reales.

```

**Características:**

### Pruebas de Integración (test_integracion.py)- Usa modelo YOLO real (`yolov8n.pt`)

- Procesa imágenes reales

Prueban la integración entre componentes reales (YOLO + OpenCV).- Valida OpenCV y YOLO juntos

- Requiere `ultralytics` instalado

**Características:**

- Usan modelo YOLO real**Ejecutar:**

- Procesan imágenes reales```bash

- Verifican integración entre componentespython tests/test_integracion.py

- Duración: ~30 segundos```



**Tests incluidos:****Pruebas incluidas:**

- Carga del modelo YOLO- Cargar modelo YOLO correctamente

- Procesamiento con modelo real- Modelo acepta frames numpy

- Detección en imagen vacía- Procesar imagen real

- Detección en imagen de prueba- Conteo retorna entero

- Estructura de resultados- Detecta mínimo 1 persona en imagen de prueba

- Codificación/decodificación base64- Validar tipo de datos de cajas

- Redimensionamiento de frames- Integración completa del flujo

- Dibujo de bounding boxes- Codificación a base64

- Texto de contador- Rendimiento de procesamiento

- Medición de performance

- Múltiples detecciones consecutivas### 3. Pruebas Funcionales (`test_funcionales.py`)

**Objetivo:** Probar el sistema completo end-to-end.

**Ejecutar:**

```bash**Características:**

python tests/test_integracion.py- Inicia servidor Django real

```- Valida estructura del proyecto

- Verifica configuraciones

### Pruebas Funcionales (test_funcionales.py)- Pruebas de sistema completo



Prueban el sistema completo end-to-end.**Ejecutar:**

```bash

**Características:**python tests/test_funcionales.py

- Verifican estructura del proyecto```

- Validan configuraciones

- Prueban integración completa**Pruebas incluidas:**

- Verifican dependencias- Servidor Django inicia correctamente

- Servidor permanece activo 5 segundos

**Tests incluidos:**- Verificar estructura del proyecto

- Estructura del proyecto- Archivos core existen

- Configuración de Django- Modelo YOLO existe

- Configuración ASGI- Django check sin errores

- Routing de WebSocket- Migraciones actualizadas

- Implementación del consumer- Configuración WebSocket

- Existencia del modelo YOLO- Templates existen

- Importación de módulos

- Dependencias instaladas## Ejecutar Todas las Pruebas

- Disponibilidad de puertos

- Configuración de Channels/Daphne### Método 1: Script personalizado

- Existencia de templates```bash

python tests/run_all_tests.py

**Ejecutar:**```

```bash

python tests/test_funcionales.py### Método 2: unittest discover

``````bash

python -m unittest discover -s tests -p "test_*.py" -v

## Ejecutar Todas las Pruebas```



### Usando el script principal### Método 3: pytest (si está instalado)

```bash

```bashpytest tests/ -v

python tests/run_all_tests.py```

```

## Dependencias Requeridas

Este script ejecuta las tres suites y muestra un resumen completo.

### Para Pruebas Unitarias:

### Usando unittest```

unittest (incluido en Python)

```bashnumpy

# Descubrir y ejecutar todas las pruebasopencv-python

python -m unittest discover -s tests -v```



# Ejecutar suite específica### Para Pruebas de Integración:

python -m unittest tests.test_unitarios -v```

python -m unittest tests.test_integracion -vultralytics

python -m unittest tests.test_funcionales -vtorch

yolov8n.pt (modelo)

# Ejecutar test específico```

python -m unittest tests.test_unitarios.TestDeteccionPersonasUnitario.test_procesar_frame_sin_personas -v

```### Para Pruebas Funcionales:

```

### Usando pytest (opcional)Django

channels

```bashdaphne

# Instalar pytest primero```

pip install pytest pytest-cov

## Configuración Previa

# Ejecutar todas las pruebas

pytest tests/ -v### 1. Instalar dependencias:

```bash

# Con cobertura de códigopip install -r requirements.txt

pytest tests/ -v --cov=core --cov-report=html```



# Ejecutar solo tests rápidos (unitarios)### 2. Preparar imagen de prueba:

pytest tests/test_unitarios.py -vColoca una imagen con personas en:

```

# Ver output detalladotests/imagenes/prueba1.jpg

pytest tests/ -v -s```

```

### 3. Verificar modelo YOLO:

## Dependencias Requeridas```bash

# Debe existir en el directorio raíz

### Para todas las pruebas:ls yolov8n.pt

``````

Django==5.2.7

numpy>=1.23,<2.0## Interpretación de Resultados

opencv-python==4.10.0.84

```### Ejemplo de salida exitosa:

```

### Para pruebas de integración:======================================================================

```EJECUTANDO PRUEBAS UNITARIAS - Detección de Personas

ultralytics==8.3.221======================================================================

torch==2.5.1test_01_... ... ok

```test_02_... ... ok

...

### Para pruebas funcionales:----------------------------------------------------------------------

```Ran 30 tests in 5.234s

channels==4.3.1

daphne==4.2.1OK

``````



## Configuración Previa### Códigos de resultado:

- **OK**: Todas las pruebas pasaron

### 1. Crear imagen de prueba- **SKIPPED**: Prueba omitida (ej: dependencia no disponible)

- **FAIL**: Prueba falló (assert no cumplido)

```bash- **ERROR**: Error durante ejecución de prueba

python tests/crear_imagen_prueba.py

```## Solución de Problemas



Esto genera `tests/imagenes/prueba1.jpg` con una figura humanoide.### Problema: "No se encuentra ultralytics"

```bash

### 2. Verificar modelo YOLOpip install ultralytics

```

Asegúrese de que `yolov8n.pt` existe en el directorio raíz del proyecto.

### Problema: "No se encuentra yolov8n.pt"

### 3. Instalar dependenciasDescarga el modelo:

```bash

```bash# Se descarga automáticamente al usar YOLO por primera vez

pip install -r requirements.txtpython -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"

``````



## Interpretación de Resultados### Problema: "Puerto en uso" en pruebas funcionales

Las pruebas usan puertos 8001 y 8002. Si están ocupados:

### Salida exitosa```bash

# Windows

```netstat -ano | findstr :8001

Ran 35 tests in 45.234staskkill /PID <PID> /F



OK# Linux/Mac

```lsof -ti:8001 | xargs kill -9

```

### Salida con errores

### Problema: "No se encuentra imagen de prueba"

``````bash

Ran 35 tests in 45.234s# Crear directorio y agregar imagen

mkdir -p tests/imagenes

FAILED (failures=2, errors=1)# Coloca una imagen con personas como tests/imagenes/prueba1.jpg

``````



### Salida con tests omitidos## Coverage (Cobertura de Código)



```Para generar reporte de cobertura:

Ran 35 tests in 45.234s

```bash

OK (skipped=6)# Instalar coverage

```pip install coverage



Los tests se omiten cuando:# Ejecutar con coverage

- Falta el modelo YOLOcoverage run -m unittest discover -s tests

- No están instaladas todas las dependencias

- No se puede configurar Django# Ver reporte

coverage report

## Solución de Problemas

# Generar HTML

### Error: "No module named 'ultralytics'"coverage html

```

```bash

pip install ultralytics## Integración Continua (CI/CD)

```

### Ejemplo para GitHub Actions:

### Error: "Modelo YOLO no encontrado"```yaml

name: Tests

Descargue el modelo:

```bashon: [push, pull_request]

python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"

```jobs:

  test:

O coloque manualmente `yolov8n.pt` en el directorio raíz.    runs-on: ubuntu-latest

    steps:

### Error: "No module named 'channels'"      - uses: actions/checkout@v2

      - name: Set up Python

```bash        uses: actions/setup-python@v2

pip install channels daphne        with:

```          python-version: '3.11'

      - name: Install dependencies

### Error: "No module named 'cv2'"        run: |

          pip install -r requirements.txt

```bash      - name: Run tests

pip install opencv-python        run: |

```          python tests/run_all_tests.py

```

### Tests muy lentos

## Notas Importantes

Las pruebas de integración pueden ser lentas en sistemas con CPU débil. Considere:

- Ejecutar solo pruebas unitarias durante desarrollo1. **Pruebas Unitarias** son las más rápidas y deben ejecutarse frecuentemente

- Usar un modelo YOLO más pequeño2. **Pruebas de Integración** requieren el modelo YOLO (puede tardar más)

- Reducir el tamaño de las imágenes de prueba3. **Pruebas Funcionales** inician el servidor completo (las más lentas)

4. Algunas pruebas se omiten automáticamente si faltan dependencias

## Coverage (Cobertura de Código)5. Las pruebas funcionales usan puertos diferentes para evitar conflictos



### Generar reporte de cobertura## Contacto



```bashPara reportar problemas con las pruebas, crear un issue en el repositorio.

# Instalar coverage

pip install coverage---



# Ejecutar tests con cobertura**Última actualización:** Noviembre 2025

coverage run -m unittest discover -s tests

# Ver reporte en terminal
coverage report

# Generar HTML
coverage html

# Abrir reporte
# Abrir htmlcov/index.html en el navegador
```

### Cobertura esperada

- core/consumers.py: >80%
- core/views.py: >90%
- core/routing.py: 100%

## Integración Continua

Para CI/CD, use este comando:

```bash
python tests/run_all_tests.py
exit_code=$?
exit $exit_code
```

### GitHub Actions (ejemplo)

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          python tests/run_all_tests.py
```

## Notas Importantes

1. Las pruebas unitarias NO requieren GPU
2. Las pruebas de integración funcionan mejor con GPU pero no es obligatorio
3. Algunos tests se omiten si faltan dependencias (comportamiento esperado)
4. El primer run puede ser lento (descarga del modelo YOLO)
5. Tests funcionales NO inician servidor real (solo verifican configuración)

## Estadísticas

- Total de tests: 35
- Tiempo promedio de ejecución: ~45 segundos
- Cobertura de código: >75%
- Compatibilidad: Python 3.11

## Contacto

Para problemas con las pruebas:
1. Verifique que todas las dependencias estén instaladas
2. Ejecute `python verificar_entorno.py`
3. Consulte la documentación principal en `README.md`
