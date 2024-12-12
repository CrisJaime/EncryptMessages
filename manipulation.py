def separar_clave(var):
    clave = [list(var[i]) for i in range(3)]
    return clave

def separar_contrasena(var, size):
    contra = var[3:]
    contra_separada = [list(contra[i]) for i in range(size)]
    return contra_separada

def manipular_indicadores(matrix, indicadores):
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
    size = len(arr) // 3
    pixels = [[arr.pop(0), arr.pop(0), arr.pop(0)] for _ in range(size)]
    return pixels

def juntar_canales(pixels, total_pixeles):
    aux = [list(pixels[i][j]) for i in range(total_pixeles) for j in range(3)]
    return aux

def manipular_contrasena(matrix, contrasena, ancho):
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
