from modules import convertions


def separar_clave(var):
    """
    Extracts the first three rows of a matrix to use as a key.
    
    Args:
        var (list): Input matrix where each row represents a group of values.
    
    Returns:
        list: List of lists containing the first three rows of the matrix.
    """
    return [list(var[i]) for i in range(3)]


def separar_contrasena(var, size):
    """
    Divides a section of the matrix into blocks of a specified size for the password.
    
    Args:
        var (list): Input matrix.
        size (int): Number of rows representing the password.
    
    Returns:
        list: List of password blocks separated into list format.
    """
    contra = var[3:]
    return [list(contra[i]) for i in range(size)]


def manipular_indicadores(matrix, indicadores):
    """
    Modifies a pixel matrix to store binary indicators.
    
    Args:
        matrix (list): Pixel matrix where the indicators will be stored.
        indicadores (list): List of binary values representing the indicators.
    
    Returns:
        list: List of modified pixels in integer format.
    """
    size_indicadores = len(indicadores) * 8
    total_pixeles = size_indicadores // 3
    pixeles_bits = [list(pixel[i]) for pixel in matrix[0][:total_pixeles] for i in range(3)]
    pixeles_bits_mod = []

    for c in range(len(indicadores)):
        byte = indicadores[c]
        start = c * 8
        end = start + 8
        for i in range(start, end):
            bit = byte[i - start]
            x = pixeles_bits[i]
            x[7] = bit
            pixeles_bits_mod.append(int(''.join(x)))
    return pixeles_bits_mod


def crear_pixeles(arr):
    """
    Converts a list of RGB values into a list of pixels in [R, G, B] format.
    
    Args:
        arr (list): List of RGB values.
    
    Returns:
        list: List of pixels in [R, G, B] format.
    """
    size = len(arr) // 3
    return [[arr.pop(0), arr.pop(0), arr.pop(0)] for _ in range(size)]


def juntar_canales(pixels, total_pixeles):
    """
    Merges the RGB channels of a list of pixels into a single array.
    
    Args:
        pixels (list): List of pixels in [R, G, B] format.
        total_pixeles (int): Total number of pixels to process.
    
    Returns:
        list: Combined list of RGB channels.
    """
    return [list(pixels[i][j]) for i in range(total_pixeles) for j in range(3)]


def manipular_contrasena(matrix, contrasena, ancho):
    """
    Modifies the pixel matrix to include a binary password.
    
    Args:
        matrix (list): Pixel matrix.
        contrasena (list): Password in binary format.
        ancho (int): Width of the image.
    
    Returns:
        list: List of modified pixels.
    """
    size = len(contrasena)
    total_bits = size * 8
    total_pixeles = total_bits // 3
    if total_pixeles > ancho:
        print(f'A larger image than {ancho} pixels in width is required.')
        print(f'The minimum width required is: {total_pixeles + 8}')
        exit()
    pixels = matrix[0][8:8 + total_pixeles]
    pixeles_separados = juntar_canales(pixels, total_pixeles)
    aux = []
    for a in range(total_bits):
        c = a // 8
        byte = pixeles_separados[a]
        bit_actual = contrasena[c][a % 8]
        byte[7] = bit_actual
        aux.append(int(''.join(byte)))
    return aux


def separacion_texto(mensaje, pixeles):
    """
    Converts the RGB values of a list of pixels into binary format.
    
    Args:
        mensaje (list): List of pixels in [R, G, B] format.
        pixeles (int): Number of pixels to process.
    
    Returns:
        list: List of RGB values in binary format.
    """
    aux = []
    for i in range(pixeles):
        r, g, b = mensaje[i]
        aux.append(list(format(r, '08b')))
        aux.append(list(format(g, '08b')))
        aux.append(list(format(b, '08b')))
    return aux


def procesar_mensaje(mensajePosicionSeparado, mensajeSeparadoBin):
    """
    Processes the message to modify the least significant bits.
    
    Args:
        mensajePosicionSeparado (list): List of binary pixel values.
        mensajeSeparadoBin (list): Binary representation of the message.
    
    Returns:
        list: List of modified binary pixel values.
    """
    aux = []
    a, b = 0, 0
    while a < len(mensajePosicionSeparado):
        byte = mensajePosicionSeparado[a]
        contador = a // 8
        if contador < len(mensajeSeparadoBin):
            mensajebyte = mensajeSeparadoBin[contador]
            bit = mensajebyte[b]
            byte[7] = bit
        aux.append(int(''.join(byte)))
        b = (b + 1) % 8
        a += 1
    return aux


def manipulacion_texto(mat, mensaje, pixels):
    """
    Modifies a pixel matrix to embed a binary message.
    
    Args:
        mat (list): Pixel matrix.
        mensaje (list): Binary representation of the message.
        pixels (int): Number of pixels required to store the message.
    
    Returns:
        list: Modified pixel matrix.
    """
    columns = len(mat[0])
    mensajeSeparadoBin = [list(m) for m in mensaje]
    totalRows = int(pixels / columns)
    aux = []
    if pixels < columns:
        mensajePosicion = mat[1][:pixels]
        mensajePosicionSeparado = separacion_texto(mensajePosicion, pixels)
        aux = procesar_mensaje(mensajePosicionSeparado, mensajeSeparadoBin)
    else:
        totalPixels = pixels
        for i in range(1, totalRows + 2):
            if totalPixels > columns:
                mensajePosicion = mat[i][:columns]
                mensajePosicionSeparado = separacion_texto(mensajePosicion, columns)
            else:
                mensajePosicion = mat[i][:totalPixels]
                mensajePosicionSeparado = separacion_texto(mensajePosicion, totalPixels)
            aux.extend(procesar_mensaje(mensajePosicionSeparado, mensajeSeparadoBin))
            totalPixels = pixels - columns
    PixelsModBin = crear_pixeles(aux)
    return convertions.bin_to_dec(PixelsModBin)


def lsb_values(bin_vals):
    """
    Extracts the least significant bit from each binary value.
    
    Args:
        bin_vals (list): List of binary values.
    
    Returns:
        list: List of least significant bits.
    """
    return [binary[-1] for binary in bin_vals]