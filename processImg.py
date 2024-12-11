from PIL import Image
import sys
import convertions

# Función para cargar una imagen
def cargar_imagen(nombre_archivo: str):
    """
    Carga una imagen desde un archivo y maneja errores si no se encuentra el archivo.
    """
    try:
        imagen = Image.open(nombre_archivo)
        print(f"[INFO] Imagen cargada exitosamente: {imagen.format}, Tamaño: {imagen.size}, Modo: {imagen.mode}")
        return imagen
    except FileNotFoundError:
        print(f'No existe una imagen con el nombre "{nombre_archivo}".')
        sys.exit(1)  # Salir con un código de error

# Extraer canales RGB de una imagen
def extraer_canales(imagen: Image.Image):
    """
    Extrae los valores RGB de cada píxel de la imagen y los organiza en una matriz.
    """
    width, height = imagen.size  # Obtener ancho y alto
    image_pixels = imagen.load()
    
    matriz = [
        [[*image_pixels[x, y]] for x in range(width)]
        for y in range(height)
    ]
    total_pixels = width * height
    return matriz, total_pixels, width, height

# Crear y mostrar una nueva imagen desde píxeles procesados
def crear_imagen(pixels, imagen_original: Image.Image, ancho: int, alto: int, conversiones):
    """
    Crea y muestra una nueva imagen utilizando los píxeles procesados.
    """
    # Convertir los píxeles en una lista de tuplas
    pixels_tuplas = conversiones.convertToDuple(pixels, ancho, alto)
    
    # Crear nueva imagen
    nueva_imagen = Image.new('RGB', (ancho, alto))
    nueva_imagen.putdata(pixels_tuplas)
    
    # Mostrar las imágenes
    nueva_imagen.show()
    imagen_original.show()
    
    return nueva_imagen
