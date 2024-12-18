from PIL import Image
import sys

# Función para cargar una imagen
def cargar_imagen(nombre_archivo: str):
    """
    Carga una imagen desde un archivo y maneja errores si el archivo no se encuentra.

    Args:
        nombre_archivo (str): Nombre del archivo de imagen (con extensión).

    Returns:
        Image.Image: Objeto de la imagen cargada si se encuentra.

    Manejo de errores:
        - Si el archivo no existe, se muestra un mensaje de error y el programa termina.

    Ejemplo:
        cargar_imagen('imagen.jpg') -> Carga y devuelve la imagen en formato PIL.Image.
    """
    try:
        imagen = Image.open(nombre_archivo)  # Abre el archivo de imagen
        print(f"[INFO] Imagen cargada exitosamente: {imagen.format}, Tamaño: {imagen.size}, Modo: {imagen.mode}")
        return imagen
    except FileNotFoundError:
        print(f'No existe una imagen con el nombre "{nombre_archivo}".')  # Manejo de error si no se encuentra el archivo
        sys.exit(1)  # Termina la ejecución con un código de error

# Extraer canales RGB de una imagen
def extraer_canales(imagen: Image.Image):
    """
    Extrae los canales RGB de cada píxel de la imagen y organiza los valores en una matriz.

    Args:
        imagen (Image.Image): Objeto de imagen cargada en formato PIL.

    Returns:
        tuple:
            - matriz (list): Matriz tridimensional que contiene los valores RGB de cada píxel.
            - total_pixels (int): Número total de píxeles en la imagen.
            - width (int): Ancho de la imagen en píxeles.
            - height (int): Alto de la imagen en píxeles.

    Ejemplo:
        extraer_canales(imagen) ->
        matriz = [[[R1, G1, B1], [R2, G2, B2], ...], ...]
        total_pixels = ancho * alto
    """
    width, height = imagen.size  # Obtener el ancho y alto de la imagen
    image_pixels = imagen.load()  # Cargar los píxeles de la imagen en memoria

    # Crear una matriz tridimensional con los valores RGB de cada píxel
    matriz = [
        [[*image_pixels[x, y]] for x in range(width)]  # Extrae [R, G, B] para cada píxel en el ancho
        for y in range(height)  # Recorre cada fila (altura de la imagen)
    ]
    total_pixels = width * height  # Calcular el total de píxeles
    return matriz, total_pixels, width, height

# Crear y mostrar una nueva imagen desde píxeles procesados
def crear_imagen(pixels, imagen_original: Image.Image, ancho: int, alto: int, conversiones):
    """
    Crea una nueva imagen utilizando los valores de píxeles procesados y la muestra junto con la imagen original.

    Args:
        pixels (list): Lista de valores RGB procesados.
        imagen_original (Image.Image): Objeto de imagen original.
        ancho (int): Ancho de la imagen en píxeles.
        alto (int): Alto de la imagen en píxeles.
        conversiones (module): Módulo con la función convertToDuple para convertir los píxeles a tuplas.

    Returns:
        Image.Image: Nueva imagen creada a partir de los píxeles proporcionados.

    Proceso:
        - Convierte la lista de píxeles en una lista de tuplas (formato [R, G, B]).
        - Crea una nueva imagen con el mismo tamaño y coloca los nuevos píxeles.
        - Muestra tanto la nueva imagen como la imagen original.

    Ejemplo:
        nueva_imagen = crear_imagen(pixels, imagen, 200, 300, conversiones)
    """
    # Convertir la lista de píxeles a tuplas RGB usando la función convertToDuple del módulo 'conversiones'
    pixels_tuplas = conversiones.convertToDuple(pixels, ancho, alto)
    
    # Crear una nueva imagen en modo RGB con las dimensiones especificadas
    nueva_imagen = Image.new('RGB', (ancho, alto))
    nueva_imagen.putdata(pixels_tuplas)  # Colocar los píxeles procesados en la nueva imagen
    
    # Mostrar las imágenes: la imagen nueva y la imagen original
    nueva_imagen.show()
    imagen_original.show()
    
    return nueva_imagen
