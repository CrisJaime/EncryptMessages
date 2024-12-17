def separar_clave(var):
    """
    Separa las primeras tres filas de la matriz var en listas individuales.
    Args:
        var (list): Matriz de entrada.
    Returns:
        list: Lista de listas que representan las primeras tres filas.
    """
    clave = [list(var[i]) for i in range(3)]
    return clave

def separar_contrasena(var, size):
    """
    Separa la contraseña en bloques individuales de tamaño especificado.
    Args:
        var (list): Matriz de entrada.
        size (int): Tamaño de cada bloque de contraseña.
    Returns:
        list: Lista de bloques de contraseña separados.
    """
    contra = var[3:]
    contra_separada = [list(contra[i]) for i in range(size)]
    return contra_separada

def manipular_indicadores(matrix, indicadores):
    """
    Manipula los indicadores de la matriz con base en los valores proporcionados.
    Args:
        matrix (list): Matriz de píxeles.
        indicadores (list): Lista de indicadores en formato binario.
    Returns:
        list: Lista de píxeles modificados.
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
    Crea una lista de píxeles a partir de una lista de valores RGB.
    Args:
        arr (list): Lista de valores RGB.
    Returns:
        list: Lista de píxeles en formato [R, G, B].
    """
    size = len(arr) // 3
    pixels = [[arr.pop(0), arr.pop(0), arr.pop(0)] for _ in range(size)]
    return pixels

def juntar_canales(pixels, total_pixeles):
    """
    Junta los canales RGB de los píxeles en una sola lista.
    Args:
        pixels (list): Lista de píxeles en formato [R, G, B].
        total_pixeles (int): Número total de píxeles a procesar.
    Returns:
        list: Lista combinada de canales.
    """
    aux = [list(pixels[i][j]) for i in range(total_pixeles) for j in range(3)]
    return aux

def manipular_contrasena(matrix, contrasena, ancho):
    """
    Manipula los píxeles de la matriz con base en la contraseña.
    Args:
        matrix (list): Matriz de píxeles.
        contrasena (list): Contraseña en formato binario.
        ancho (int): Ancho de la imagen.
    Returns:
        list: Lista de píxeles modificados.
    """
    size = len(contrasena)
    total_bits = size * 8
    total_pixeles = total_bits // 3

    if total_pixeles > ancho:
        print(f'Se necesita una imagen más grande que {ancho} píxeles de ancho.')
        print(f'El mínimo de píxeles de ancho es: {total_pixeles + 8}')
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
    Convierte los valores RGB de los píxeles a formato binario.
    Args:
        mensaje (list): Lista de píxeles en formato [R, G, B].
        pixeles (int): Número de píxeles a procesar.
    Returns:
        list: Lista de valores RGB en formato binario.
    """
    aux = []
    for i in range(pixeles):
        r, g, b = mensaje[i][0], mensaje[i][1], mensaje[i][2]
        rb, gb, bb = list(format(r, '08b')), list(format(g, '08b')), list(format(b, '08b'))
        aux.append(rb)
        aux.append(gb)
        aux.append(bb)
    return aux
