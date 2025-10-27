# Sistema_De_Deteccion_de_Personas

¡Bienvenido! Este es un proyecto en Django que implementa un sistema de **detección de personas en tiempo real** utilizando WebSockets (Django Channels).

El sistema procesa un stream de video, cuenta el número de personas detectadas y envía tanto el video procesado como el conteo al navegador en tiempo real.

## 🚀 Características Principales

* **Detección en Tiempo Real:** Procesa un stream de video (usando OpenCV, YOLO, etc.) para detectar y contar personas.
* **Streaming por WebSockets:** Utiliza Django Channels y Daphne para enviar el video (frame por frame) y los datos (conteo) al frontend sin necesidad de recargar la página.
* **Control de Estado:** El usuario puede iniciar y detener el stream de detección desde el navegador.
* **(Opcional: Añade esto si es relevante)** **Módulo de Grabación de Audio:** Incluye una funcionalidad separada para capturar audio desde el micrófono del usuario y enviarlo al servidor.

## 🛠️ Tecnologías Utilizadas

* **Backend:**
    * Python
    * Django
    * Django Channels (para WebSockets)
    * Daphne (servidor ASGI)
    * OpenCv
    * Yolo
* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript 

---

## ⚙️ Instalación y Puesta en Marcha

Sigue estos pasos para tener una copia local del proyecto funcionando.

### Prerrequisitos

* Python 3.8 o superior
* Pip (manejador de paquetes de Python)

### Pasos

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Janzam/DetencionPersonas-.git
    cd DetencionPersonas-.


2.  **(Recomendado) Crea y activa un entorno virtual:**
    * En Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * En macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta las migraciones de Django:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicia el servidor:**
    (Django Channels/Daphne se inician con `runserver`)
    ```bash
    python manage.py runserver
    ```

---

## 🏃‍♂️ Uso

1.  Una vez que el servidor esté corriendo, abre tu navegador.
2.  Ve a `http://127.0.0.1:8000/` (o la URL principal de tu app).
3.  Haz clic en el botón **"Iniciar Detección"**.
4.  Deberías ver el stream de video y el contador de personas actualizarse en vivo.

---



Enlace del Proyecto: https://github.com/Janzam/DetencionPersonas-.git
