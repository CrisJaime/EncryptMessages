# Caches for storing precomputed values, used to improve the efficiency of conversions.
convertASCIICache = {}
decToBinCache = {}
coloToBinCache = {}
binToDecCache = {}

# Convert ASCII characters
def convert_ascii(contra: str) -> list:
    """
    Converts a string into a list of ASCII values.
    Uses a cache to avoid recalculating already processed values.

    Args:
        contra (str): String to convert.

    Returns:
        list: List of ASCII values corresponding to each character in the string.
    """
    return [convertASCIICache.setdefault(c, ord(c)) for c in contra]

# Convert decimals to binary
def dec_to_bin(ascii_vals: list) -> list:
    """
    Converts a list of decimal (ASCII) values into a list of binary
    8-bit values, using a cache for optimization.

    Args:
        ascii_vals (list): List of decimal (ASCII) values.

    Returns:
        list: List of 8-bit binary strings representing the decimal values.
    """
    return [decToBinCache.setdefault(a, format(a, '08b')) for a in ascii_vals]

# Convert RGB colors to binary
def color_to_bin(arr: list, ancho: int, alto: int) -> list:
    """
    Converts a matrix of RGB colors (in decimal format) into a matrix of binary
    8-bit values for each component (R, G, B).

    Args:
        arr (list): Matrix of RGB colors with dimensions [height][width][3].
        ancho (int): Image width in pixels.
        alto (int): Image height in pixels.

    Returns:
        list: Matrix of binary values corresponding to each RGB component.
    """
    return [
        [
            [
                coloToBinCache.setdefault(color, format(color, '08b'))  # Converts each component to binary.
                for color in pixel  # Processes each component (R, G, B) of the pixel.
            ]
            for pixel in row  # Processes each pixel in the row.
        ]
        for row in arr  # Processes each row in the matrix.
    ]

# Convert binary to decimals
def bin_to_dec(arr: list) -> list:
    """
    Converts a list of binary RGB values back into their original decimal values.
    Optimizes the process using a cache to avoid repeated conversions.

    Args:
        arr (list): Matrix of binary RGB values with dimensions [height][width][3].

    Returns:
        list: Matrix of decimal values corresponding to each RGB component.
    """
    return [
        [
            binToDecCache.setdefault(str(value), int(str(value), 2))  # Converts the binary value to decimal.
            for value in pixel  # Processes each component (R, G, B) of the pixel.
        ]
        for pixel in arr  # Processes each row of pixels.
    ]

# Convert a list of matrices into a list of tuples
def convert_to_duple(lista: list, ancho: int, alto: int) -> list:
    """
    Converts a matrix of RGB values (or any nested matrix) into a flat list
    of tuples, where each tuple represents a pixel with its components.

    Args:
        lista (list): Matrix of values with dimensions [height][width][3].
        ancho (int): Matrix width in pixels.
        alto (int): Matrix height in pixels.

    Returns:
        list: Flat list of tuples (R, G, B) representing the matrix's pixels.
    """
    return [tuple(lista[i][j]) for i in range(alto) for j in range(ancho)]
