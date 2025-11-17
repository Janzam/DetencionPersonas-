""""""

Script para crear imágenes de prueba con figuras humanoidesScript para crear una imagen de prueba sintética con personas simuladas

"""Útil si no tienes una imagen real para pruebas

"""

import cv2import cv2

import numpy as npimport numpy as np

import osimport os





def crear_imagen_con_persona():def crear_imagen_prueba():

    """Crear una imagen con una figura humanoide simple"""    """Crea una imagen sintética para pruebas"""

    # Crear imagen blanca    

    img = np.ones((480, 640, 3), dtype=np.uint8) * 255    # Crear imagen en blanco

        img = np.ones((480, 640, 3), dtype=np.uint8) * 255

    # Dibujar figura humana simple    

    # Cabeza    # Simular 2 "personas" con rectángulos y características básicas

    cv2.circle(img, (320, 100), 40, (0, 0, 0), -1)    

        # Persona 1

    # Cuerpo (rectángulo)    cv2.rectangle(img, (100, 150), (200, 400), (100, 100, 200), -1)  # Cuerpo

    cv2.rectangle(img, (280, 140), (360, 300), (0, 0, 0), -1)    cv2.circle(img, (150, 120), 30, (200, 150, 100), -1)  # Cabeza

        

    # Brazos    # Persona 2

    cv2.rectangle(img, (220, 140), (280, 180), (0, 0, 0), -1)  # Brazo izquierdo    cv2.rectangle(img, (350, 180), (430, 420), (150, 120, 180), -1)  # Cuerpo

    cv2.rectangle(img, (360, 140), (420, 180), (0, 0, 0), -1)  # Brazo derecho    cv2.circle(img, (390, 150), 25, (180, 160, 120), -1)  # Cabeza

        

    # Piernas    # Agregar texto

    cv2.rectangle(img, (280, 300), (310, 400), (0, 0, 0), -1)  # Pierna izquierda    cv2.putText(img, "Imagen de Prueba", (10, 30), 

    cv2.rectangle(img, (330, 300), (360, 400), (0, 0, 0), -1)  # Pierna derecha                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        cv2.putText(img, "2 personas simuladas", (10, 60), 

    return img                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    

    # Guardar imagen

def main():    output_dir = os.path.join(os.path.dirname(__file__), 'imagenes')

    """Crear y guardar imágenes de prueba"""    os.makedirs(output_dir, exist_ok=True)

    # Crear directorio de imágenes si no existe    

    script_dir = os.path.dirname(os.path.abspath(__file__))    output_path = os.path.join(output_dir, 'prueba1.jpg')

    imagenes_dir = os.path.join(script_dir, 'imagenes')    cv2.imwrite(output_path, img)

        

    if not os.path.exists(imagenes_dir):    print(f"✓ Imagen de prueba creada: {output_path}")

        os.makedirs(imagenes_dir)    print(f"  Dimensiones: {img.shape}")

        print(f"Directorio creado: {imagenes_dir}")    print(f"  Tamaño: {os.path.getsize(output_path)} bytes")

        

    # Crear y guardar imagen    return output_path

    img = crear_imagen_con_persona()

    output_path = os.path.join(imagenes_dir, 'prueba1.jpg')

    cv2.imwrite(output_path, img)if __name__ == '__main__':

        print("=" * 60)

    print(f"Imagen de prueba creada: {output_path}")    print("Creando imagen de prueba sintética")

    print("Dimensiones: 640x480")    print("=" * 60)

    print("Contenido: Figura humanoide simple")    

    ruta = crear_imagen_prueba()

    

if __name__ == '__main__':    print("\n✓ ¡Listo! Ahora puedes ejecutar las pruebas de integración.")

    main()    print(f"\nNOTA: Esta es una imagen sintética. Para mejores pruebas,")

    print(f"      reemplaza '{ruta}' con una imagen real que contenga personas.")
