from PIL import Image

from modules import convertions

def insertar_mensaje_en_pixeles(pixels, pixels_modificados_dec, total_pixels_texto, pixels_indicadores_dec, ancho, alto):
    """
    Inserts a message into the pixels of an image and adds indicators at the end of the message.

    Args:
        pixels (list): Matrix of the image pixels.
        pixels_modificados_dec (list): Modified pixels containing the binary message.
        total_pixels_texto (int): Total number of pixels required for the message.
        pixels_indicadores_dec (list): Indicator pixels to mark the end of the message.
        ancho (int): Width of the image.
        alto (int): Height of the image.

    Returns:
        list: Updated pixel matrix with the inserted message.
    """
    if total_pixels_texto > (alto * ancho):
        print('The message exceeds the available pixel capacity of the image.')
        exit()

    total_filas = -(-total_pixels_texto // ancho)  # Equivalent to math.ceil
    cantidad_restante = total_pixels_texto
    
    for fila in range(total_filas):
        inicio = fila * ancho
        fin = min(inicio + ancho, total_pixels_texto)
        if cantidad_restante > ancho:
            pixels[fila + 1] = pixels_modificados_dec[inicio:fin]
        else:
            pixels[fila + 1][:cantidad_restante] = pixels_modificados_dec[inicio:inicio + cantidad_restante]
            pixels[fila + 1][cantidad_restante:cantidad_restante + 8] = pixels_indicadores_dec
        cantidad_restante -= ancho

    print("[INFO] Pixels Created")
    return pixels

def open_image(image_path):
    """
    Opens and displays the image from the provided path.

    Args:
        image_path (str): Path to the image file.

    Returns:
        PIL.Image: Opened image object.
    """
    try:
        img = Image.open(image_path)
        print(f"[INFO] Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
        img.show()
        return img
    except FileNotFoundError:
        print(f"[ERROR] The image with the file '{image_path}' was not found.")
    except Exception as e:
        print(f"[ERROR] Could not open the image: {e}")

def extraer_canales(image):
    """
    Extracts the RGB values from each pixel of the image and organizes them into a matrix.

    Args:
        image (PIL.Image): Input image object.

    Returns:
        tuple: (Pixel matrix, total number of pixels, width, height)
    """
    width, height = image.size
    image_pixels = list(image.getdata())
    matriz = [image_pixels[i * width:(i + 1) * width] for i in range(height)]
    total_pixels = len(image_pixels)
    return matriz, total_pixels, width, height

def crear_imagen(pixels, ancho, alto):
    """
    Creates a new image using the processed pixels.

    Args:
        pixels (list): List of processed pixels (in tuple format).
        ancho (int): Width of the new image.
        alto (int): Height of the new image.

    Returns:
        PIL.Image: A new image created from the processed pixels.
    """
    pixels_tuplas = convertions.convert_to_duple(pixels, ancho, alto)
    nueva_imagen = Image.new('RGB', (ancho, alto))
    nueva_imagen.putdata(pixels_tuplas)
    print("[INFO] New image created")
    return nueva_imagen

def final_pixels(pixels, textPixels, columns):
    """
    Inserts text pixels into the image pixel matrix.

    Args:
        pixels (list): Matrix of the image pixels.
        textPixels (list): Pixels representing the text.
        columns (int): Number of columns in the image.

    Returns:
        list: Updated pixel matrix containing the text.
    """
    totalColumns = len(textPixels)
    totalRows = totalColumns / columns
    
    if totalRows < 1:
        pixels[1][0:len(textPixels)] = textPixels
    else:
        for i in range(1, round(totalRows) + 2):
            residualColumns = len(textPixels)
            if residualColumns > columns:
                pixels[i] = textPixels[0:columns]
                del textPixels[:columns]
            else:
                pixels[i][0:residualColumns] = textPixels
    return pixels
