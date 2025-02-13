from modules import convertions

def separar_clave(var):
    """
    Extracts the first three rows of a matrix to use as a key.
    
    Args:
        var (list): Input matrix where each row represents a group of values.
    
    Returns:
        list: List of lists containing the first three rows of the matrix.
    """
    clave = [list(var[i]) for i in range(3)]
    return clave

def separar_contrasena(var, size):
    """
    Divides a section of the matrix into blocks of a specified size for the password.
    
    Args:
        var (list): Input matrix.
        size (int): Number of rows representing the password.
    
    Returns:
        list: List of password blocks separated into list format.
    """
    contra = var[3:]  # Skip the first three rows.
    contra_separada = [list(contra[i]) for i in range(size)]
    return contra_separada

def manipular_indicadores(matrix, indicadores):
    """
    Modifies a pixel matrix to store binary indicators.
    
    Args:
        matrix (list): Pixel matrix where the indicators will be stored.
        indicadores (list): List of binary values representing the indicators.
    
    Returns:
        list: List of modified pixels in integer format.
    """
    size_indicadores = len(indicadores) * 8  # Total size of the indicators in bits.
    total_pixeles = size_indicadores // 3  # Number of pixels needed to store the indicators.
    
    # Extracts the pixels and divides them into RGB channels.
    pixeles_bits = [list(pixel[i]) for pixel in matrix[0][:total_pixeles] for i in range(3)]
    pixeles_bits_mod = []

    for c in range(len(indicadores)):
        byte = indicadores[c]
        start = c * 8
        end = start + 8
        for i in range(start, end):
            bit = byte[i - start]  # Gets each bit of the indicator.
            x = pixeles_bits[i]  # Modifies the corresponding byte in the pixels.
            x[7] = bit
            pixeles_bits_mod.append(int(''.join(x)))  # Converts the modified byte to integer.
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
    pixels = [[arr.pop(0), arr.pop(0), arr.pop(0)] for _ in range(size)]
    return pixels

def juntar_canales(pixels, total_pixeles):
    """
    Merges the RGB channels of a list of pixels into a single array.
    
    Args:
        pixels (list): List of pixels in [R, G, B] format.
        total_pixeles (int): Total number of pixels to process.
    
    Returns:
        list: Combined list of RGB channels.
    """
    aux = [list(pixels[i][j]) for i in range(total_pixeles) for j in range(3)]
    return aux

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

    # Verifies if the image width is sufficient to store the password.
    if total_pixeles > ancho:
        print(f'A larger image than {ancho} pixels in width is required.')
        print(f'The minimum width required is: {total_pixeles + 8}')
        exit()

    # Extracts and separates the pixels needed to store the password.
    pixels = matrix[0][8:8 + total_pixeles]
    pixeles_separados = juntar_canales(pixels, total_pixeles)

    aux = []
    for a in range(total_bits):
        c = a // 8  # Index of the byte in the password.
        byte = pixeles_separados[a]
        bit_actual = contrasena[c][a % 8]  # Gets the corresponding bit of the password.
        byte[7] = bit_actual  # Modifies the least significant bit of the byte.
        aux.append(int(''.join(byte)))  # Converts the modified byte to integer.

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
        r, g, b = mensaje[i][0], mensaje[i][1], mensaje[i][2]
        rb, gb, bb = list(format(r, '08b')), list(format(g, '08b')), list(format(b, '08b'))
        aux.append(rb)
        aux.append(gb)
        aux.append(bb)
    return aux

def procesar_mensaje(mensajePosicionSeparado,mensajeSeparadoBin):
    aux = []
    a, b = 0, 0
    
    while a < len(mensajePosicionSeparado):
        byte = mensajePosicionSeparado[a]
        contador = a // 8
        
        if contador < len(mensajeSeparadoBin):
            mensajebyte = mensajeSeparadoBin[contador]
            bit = mensajebyte[b]
            byte[7] = bit  # Modifica el último bit del byte
        
        aux.append(int(''.join(byte)))  # Convierte la lista de caracteres en un número
        b = (b + 1) % 8
        a += 1
    
    return aux

def manipulacion_texto(mat, mensaje, pixels):
    """
    Modifies a pixel matrix to embed a binary message.
    
    Args:
        mat (list): Pixel matrix.
        mensaje (list): Message in binary format.
        pixeles (int): Number of pixels required to store the message.
    
    Returns:
        list: Modified pixel matrix.
    """
    columns = len(mat[0])  # image_width of the image.
    #rows= len(mat) # image_height of the image. 
    mensajeSeparadoBin = [list(m) for m in mensaje] #Mensaje separado en Binario
    totalRows=int(pixels/columns)
    # print(pixels,columns,totalRows)
    
    aux = []  # Lista para almacenar el resultado de procesar_mensaje
    
    if pixels < columns:
        # Case 1: The message fits in a single row.
        mensajePosicion = mat[1][:pixels]
        mensajePosicionSeparado = separacion_texto(mensajePosicion, pixels)
        aux=procesar_mensaje(mensajePosicionSeparado,mensajeSeparadoBin)
    else: 
        # Case 2: The message spans multiple rows.
        totalPixels=pixels
        for i in range(1,totalRows+2):
            if totalPixels > columns:
                mensajePosicion=mat[i][:columns]
                mensajePosicionSeparado = separacion_texto(mensajePosicion,columns)
            else:
                mensajePosicion=mat[i][:totalPixels]
                mensajePosicionSeparado = separacion_texto(mensajePosicion,totalPixels)
            # print(totalPixels,i,len(mensajePosicion),len(mensajePosicionSeparado))
            
            # Acumular los resultados en aux
            aux.extend(procesar_mensaje(mensajePosicionSeparado, mensajeSeparadoBin))
            
            totalPixels=pixels-columns
    
    PixelsModBin = crear_pixeles(aux)  # Converts to binary format.
    PixelsModDec = convertions.bin_to_dec(PixelsModBin)  # Converts to decimal format.  
    
    # print(mat[1][:10])
    # print(PixelsModDec[:10])
    return PixelsModDec
    
def lsb_values(bin_vals: list)-> list:
    lsb_values = [binary[-1] for binary in bin_vals]
    return lsb_values
    