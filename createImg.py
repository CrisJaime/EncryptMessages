from PIL import Image

import convertions

def insertar_mensaje_en_pixeles(pixels, pixels_modificados_dec, total_pixels_texto, pixels_indicadores_dec, ancho, alto):
    """
    Inserta un mensaje en los píxeles de una imagen y añade indicadores al final del mensaje.
    
    Args:
        pixels (list): Matriz de píxeles de la imagen.
        pixels_modificados (list): Píxeles modificados que contienen el mensaje binario.
        total_pixels_texto (int): Total de píxeles necesarios para el mensaje.
        pixels_indicadores (list): Píxeles indicadores para marcar el fin del mensaje.
        ancho (int): Ancho de la imagen.
        alto (int): Alto de la imagen.

    Returns:
        list: Matriz de píxeles actualizada con el mensaje insertado.
    """
    if total_pixels_texto > (alto * ancho):
        print('El texto supera la cantidad de píxeles de la imagen')
        exit()

    # Cálculo del número de filas necesarias
    total_filas = -(-total_pixels_texto // ancho)  # Redondeo hacia arriba (equivalente a math.ceil)

    # Inserción del mensaje
    cantidad_restante = total_pixels_texto
    for fila in range(total_filas):
        inicio = fila * ancho
        fin = min(inicio + ancho, total_pixels_texto)
        if cantidad_restante > ancho:
            pixels[fila + 1] = pixels_modificados_dec[inicio:fin]
        else:
            pixels[fila + 1][:cantidad_restante] = pixels_modificados_dec[inicio:inicio + cantidad_restante]
            # Añadir indicadores al final del mensaje
            pixels[fila + 1][cantidad_restante:cantidad_restante + 8] = pixels_indicadores_dec
        cantidad_restante -= ancho

    print("[INFO] Pixeles Creados")
    return pixels


def open_image(image_path):
    """
    Abre y muestra la imagen desde la ruta proporcionada.
    
    Args:
        image_path (str): Ruta del archivo de imagen.
    """
    try:
        # Abre la imagen
        img = Image.open(image_path)
        print(f"[INFO] Formato: {img.format}, Tamaño: {img.size}, Modo: {img.mode}")
        img.show()
        return img
    except FileNotFoundError:
        print(f"[ERROR] La imagen con el archivo '{image_path}' no se encuentra.")
    except Exception as e:
        print(f"[ERROR] No se pudo abrir la imagen: {e}")
        
def extraer_canales(image):
    """
    Extrae los valores RGB de cada píxel de la imagen y los organiza en una matriz.
    
    Args:
        image (PIL.Image): Objeto de la imagen de entrada.
    
    Returns:
        tuple: Contiene la matriz de píxeles, el total de píxeles, el ancho y el alto.
    """
    width, height = image.size  # Obtener ancho y alto
    image_pixels = list(image.getdata())  # Obtener todos los píxeles de la imagen
    
    # Convertir los píxeles a una matriz de 2 dimensiones
    matriz = [image_pixels[i * width:(i + 1) * width] for i in range(height)]
    
    total_pixels = len(image_pixels)
    return matriz, total_pixels, width, height


def crear_imagen(pixels, imagen_original, ancho, alto):
    """
    Crea y muestra una nueva imagen utilizando los píxeles procesados.
    
    Args:
        pixels (list): Lista de píxeles procesados (en formato de tuplas).
        imagen_original (PIL.Image): Imagen original para mostrarla junto a la nueva.
        ancho (int): Ancho de la nueva imagen.
        alto (int): Alto de la nueva imagen.
    
    Returns:
        PIL.Image: Nueva imagen creada a partir de los píxeles procesados.
    """
    # Convertir los píxeles en una lista de tuplas (RGB)
    pixels_tuplas = convertions.convert_to_duple(pixels, ancho, alto)
    
    # Crear una nueva imagen con los píxeles procesados
    nueva_imagen = Image.new('RGB', (ancho, alto))
    nueva_imagen.putdata(pixels_tuplas)
    
    # Mostrar las imágenes
    print("[INFO] Imagen nueva creada")
    nueva_imagen.show()
    imagen_original.show()
    
    return nueva_imagen