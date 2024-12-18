# Cachés para almacenamiento de valores precomputados, utilizados para mejorar la eficiencia de las conversiones.
convertASCIICache = {}
decToBinCache = {}
coloToBinCache = {}
binToDecCache = {}

# Convertir caracteres ASCII


def convert_ascii(contra: str) -> list:
    """
    Convierte una cadena de texto en una lista de valores ASCII.
    Utiliza un caché para evitar recalcular valores ya procesados.

    Args:
        contra (str): Cadena de texto a convertir.

    Returns:
        list: Lista de valores ASCII correspondientes a cada carácter de la cadena.
    """
    return [convertASCIICache.setdefault(c, ord(c)) for c in contra]

# Convertir decimales a binarios


def dec_to_bin(ascii_vals: list) -> list:
    """
    Convierte una lista de valores decimales (ASCII) a una lista de valores binarios
    de 8 bits, utilizando un caché para optimización.

    Args:
        ascii_vals (list): Lista de valores decimales (ASCII).

    Returns:
        list: Lista de cadenas binarias de 8 bits que representan los valores decimales.
    """
    return [decToBinCache.setdefault(a, format(a, '08b')) for a in ascii_vals]

# Convertir colores RGB a binarios


def color_to_bin(arr: list, ancho: int, alto: int) -> list:
    """
    Convierte una matriz de colores RGB (en formato decimal) a una matriz de valores binarios 
    de 8 bits por componente (R, G, B).

    Args:
        arr (list): Matriz de colores RGB con dimensiones [alto][ancho][3].
        ancho (int): Ancho de la imagen en píxeles.
        alto (int): Alto de la imagen en píxeles.

    Returns:
        list: Matriz de valores binarios correspondientes a cada componente RGB.
    """
    return [
        [
            [
                coloToBinCache.setdefault(color, format(color, '08b'))  # Convierte cada componente a binario.
                for color in pixel  # Procesa cada componente (R, G, B) del píxel.
            ]
            for pixel in fila  # Procesa cada píxel de la fila.
        ]
        for fila in arr  # Procesa cada fila de la matriz.
    ]

# Convertir binarios a decimales


def bin_to_dec(arr: list) -> list:
    """
    Convierte una lista de valores binarios RGB a sus valores decimales originales.
    Optimiza el proceso con un caché para evitar conversiones repetidas.

    Args:
        arr (list): Matriz de valores binarios RGB con dimensiones [alto][ancho][3].

    Returns:
        list: Matriz de valores decimales correspondientes a cada componente RGB.
    """
    return [
        [
            binToDecCache.setdefault(str(value), int(str(value), 2))  # Convierte el valor binario a decimal.
            for value in pixel  # Procesa cada componente (R, G, B) del píxel.
        ]
        for pixel in arr  # Procesa cada fila de píxeles.
    ]

# Convertir una lista de matrices a una lista de tuplas


def convert_to_duple(lista: list, ancho: int, alto: int) -> list:
    """
    Convierte una matriz de valores RGB (o cualquier matriz anidada) a una lista plana 
    de tuplas, donde cada tupla representa un píxel con sus componentes.

    Args:
        lista (list): Matriz de valores con dimensiones [alto][ancho][3].
        ancho (int): Ancho de la matriz en píxeles.
        alto (int): Alto de la matriz en píxeles.

    Returns:
        list: Lista plana de tuplas (R, G, B) que representan los píxeles de la matriz.
    """
    return [tuple(lista[i][j]) for i in range(alto) for j in range(ancho)]
