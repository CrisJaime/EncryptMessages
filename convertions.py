# Cachés para almacenamiento de valores precomputados
convertASCIICache = {}
decToBinCache = {}
coloToBinCache = {}
binToDecCache = {}

# Convertir caracteres ASCII


def convert_ascii(contra: str) -> list:
    """
    Convierte una cadena en una lista de valores ASCII, utilizando un caché para optimización.
    """
    return [convertASCIICache.setdefault(c, ord(c)) for c in contra]

# Convertir decimales a binarios


def dec_to_bin(ascii_vals: list) -> list:
    """
    Convierte una lista de valores ASCII en binarios de 8 bits, con optimización mediante caché.
    """
    return [decToBinCache.setdefault(a, format(a, '08b')) for a in ascii_vals]

# Convertir colores RGB a binarios


def color_to_bin(arr: list, ancho: int, alto: int) -> list:
    """
    Convierte una matriz de colores RGB en una matriz de valores binarios de 8 bits.
    """
    return [
        [
            [
                coloToBinCache.setdefault(color, format(color, '08b'))
                for color in pixel
            ]
            for pixel in fila
        ]
        for fila in arr
    ]

# Convertir binarios a decimales


def bin_to_dec(arr: list) -> list:
    """
    Convierte una lista de valores binarios RGB en decimales, optimizando con un caché.
    """
    return [
        [
            binToDecCache.setdefault(str(value), int(str(value), 2)) for value in pixel
        ]
        for pixel in arr
    ]

# Convertir una lista de matrices a una lista de tuplas


def convert_to_duple(lista: list, ancho: int, alto: int) -> list:
    """
    Convierte una matriz de valores en una lista de tuplas (representación plana).
    """
    return [tuple(lista[i][j]) for i in range(alto) for j in range(ancho)]
