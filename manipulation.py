import convertions

def separar_clave(var):
    """
    Extrae las primeras tres filas de una matriz para utilizarlas como clave.
    
    Args:
        var (list): Matriz de entrada, donde cada fila representa un grupo de valores.
    
    Returns:
        list: Lista de listas que contienen las primeras tres filas de la matriz.
    """
    clave = [list(var[i]) for i in range(3)]
    return clave

def separar_contrasena(var, size):
    """
    Divide una sección de la matriz en bloques de tamaño especificado para la contraseña.
    
    Args:
        var (list): Matriz de entrada.
        size (int): Cantidad de filas que representan la contraseña.
    
    Returns:
        list: Lista de bloques de contraseña separados en formato de lista.
    """
    contra = var[3:]  # Omite las primeras tres filas.
    contra_separada = [list(contra[i]) for i in range(size)]
    return contra_separada

def manipular_indicadores(matrix, indicadores):
    """
    Modifica una matriz de píxeles para almacenar indicadores binarios.
    
    Args:
        matrix (list): Matriz de píxeles donde se almacenarán los indicadores.
        indicadores (list): Lista de valores binarios representando los indicadores.
    
    Returns:
        list: Lista de píxeles modificados en formato entero.
    """
    size_indicadores = len(indicadores) * 8  # Tamaño total de los indicadores en bits.
    total_pixeles = size_indicadores // 3  # Número de píxeles necesarios para almacenar los indicadores.
    
    # Extrae los píxeles y los divide en canales RGB.
    pixeles_bits = [list(pixel[i]) for pixel in matrix[0][:total_pixeles] for i in range(3)]
    pixeles_bits_mod = []

    for c in range(len(indicadores)):
        byte = indicadores[c]
        start = c * 8
        end = start + 8
        for i in range(start, end):
            bit = byte[i - start]  # Obtiene cada bit del indicador.
            x = pixeles_bits[i]  # Modifica el byte correspondiente en los píxeles.
            x[7] = bit
            pixeles_bits_mod.append(int(''.join(x)))  # Convierte el byte modificado a entero.

    return pixeles_bits_mod

def crear_pixeles(arr):
    """
    Convierte una lista de valores RGB a una lista de píxeles en formato [R, G, B].
    
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
    Une los canales RGB de una lista de píxeles en un solo arreglo.
    
    Args:
        pixels (list): Lista de píxeles en formato [R, G, B].
        total_pixeles (int): Número total de píxeles a procesar.
    
    Returns:
        list: Lista combinada de canales RGB.
    """
    aux = [list(pixels[i][j]) for i in range(total_pixeles) for j in range(3)]
    return aux

def manipular_contrasena(matrix, contrasena, ancho):
    """
    Modifica la matriz de píxeles para incluir una contraseña binaria.
    
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

    # Verifica si el ancho de la imagen es suficiente para almacenar la contraseña.
    if total_pixeles > ancho:
        print(f'Se necesita una imagen más grande que {ancho} píxeles de ancho.')
        print(f'El mínimo de píxeles de ancho es: {total_pixeles + 8}')
        exit()

    # Extrae y separa los píxeles necesarios para almacenar la contraseña.
    pixels = matrix[0][8:8 + total_pixeles]
    pixeles_separados = juntar_canales(pixels, total_pixeles)

    aux = []
    for a in range(total_bits):
        c = a // 8  # Índice del byte en la contraseña.
        byte = pixeles_separados[a]
        bit_actual = contrasena[c][a % 8]  # Obtiene el bit correspondiente de la contraseña.
        byte[7] = bit_actual  # Modifica el bit menos significativo del byte.
        aux.append(int(''.join(byte)))  # Convierte el byte modificado a entero.

    return aux

def separacion_texto(mensaje, pixeles):
    """
    Convierte los valores RGB de una lista de píxeles a formato binario.
    
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

def manipulacion_texto(mat, mensaje, pixeles):
    """
    Modifica una matriz de píxeles para incrustar un mensaje binario.
    
    Args:
        mat (list): Matriz de píxeles.
        mensaje (list): Mensaje en formato binario.
        pixeles (int): Cantidad de píxeles necesarios para almacenar el mensaje.
    
    Returns:
        list: Matriz de píxeles modificada.
    """
    sizeMat = len(mat[0])  # Ancho de la imagen.
    mensajeSeparado = [list(m) for m in mensaje]
    aux = []

    if pixeles < sizeMat:
        # Caso 1: El mensaje cabe en una fila.
        mensajePosicion = mat[1][:pixeles]
        mensajePosicionSeparado = separacion_texto(mensajePosicion, pixeles)

        a, b = 0, 0
        while a < len(mensajePosicionSeparado):
            byte = mensajePosicionSeparado[a]
            contador = a // 8
            if contador < len(mensajeSeparado):
                mensajebyte = mensajeSeparado[contador]
                bit = mensajebyte[b]
                byte[7] = bit
            aux.append(int(''.join(byte)))
            b = (b + 1) % 8
            a += 1
    else:
        # Caso 2: El mensaje ocupa varias filas.
        totalDeFilas = -(-pixeles // sizeMat)  # Redondeo hacia arriba.
        for i in range(totalDeFilas):
            fila_pixeles = min(sizeMat, pixeles)
            mensajePosicion = mat[i + 1][:fila_pixeles]
            mensajePosicionSeparado = separacion_texto(mensajePosicion, fila_pixeles)

            a, b = 0, 0
            while a < len(mensajePosicionSeparado):
                byte = mensajePosicionSeparado[a]
                contador = a // 8
                if contador < len(mensajeSeparado):
                    mensajebyte = mensajeSeparado[contador]
                    bit = mensajebyte[b]
                    byte[7] = bit
                aux.append(int(''.join(byte)))
                b = (b + 1) % 8
                a += 1
            pixeles -= sizeMat

    PixelsModBin = crear_pixeles(aux)  # Convierte a formato binario.
    PixelsModDec = convertions.bin_to_dec(PixelsModBin)  # Convierte a formato decimal.
    return PixelsModDec
