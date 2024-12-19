import string
import random
import os
from typing import List

# Generate a secure password with letters, numbers, and special characters
def crear_contrasena(n: int) -> str:
    """
    Generates a secure password of length n, combining letters, numbers, and special characters.

    The password always starts with three special characters ('@', '^', '#'),
    followed by a random combination of letters and numbers.

    Args:
        n (int): Total length of the generated password.

    Returns:
        str: Randomly generated password.

    Example:
        crear_contrasena(10) -> "@^#aB2cD3E4"
    """
    caracteres = string.ascii_letters + string.digits  # Uppercase, lowercase letters, and digits
    contrasena = '@^#' + ''.join(random.choice(caracteres) for _ in range(n))  # Random characters
    print("[INFO] Password generated successfully.")
    return contrasena

# Create a 'Llave.txt' file with a list of lines
def crear_archivo(contenido: List[str]) -> None:
    """
    Creates a file named 'Llave.txt' and writes the provided lines to it.

    Args:
        contenido (List[str]): List of lines to write into the file.

    The file is saved in the `Files` folder.

    Example:
        crear_archivo(["line 1\n", "line 2\n"])

    Result:
        'Llave.txt' file with the following content:
        line 1
        line 2
    """
    output_dir = 'data\\output\\txt'
    file_path = os.path.join(output_dir, 'key.txt')

    with open(file_path, 'w') as archivo:
        archivo.writelines(contenido)  # Write the lines to the file
    print("[INFO] Password file 'key.txt' created successfully.")

# Create a 'cambios.txt' file based on pixel values and message size
def crear_archivo_cambios(pixels: List[List[int]], filas: int, ancho: int, len_texto: int) -> None:
    """
    Creates a file named 'cambios.txt' containing information about modified pixels.

    Args:
        pixels (List[List[int]]): Two-dimensional list representing RGB values of pixels.
        filas (int): Number of rows in the pixel matrix.
        ancho (int): Number of pixels per row (image width).
        len_texto (int): Length of the message to be processed in pixels.

    The file is saved in the Files folder.

    Process:
    - Writes the first line of the file with the first 88 pixels of the matrix.
    - For subsequent rows, includes the required number of pixels based on the remaining message size (len_texto + 8).

    Example:
        crear_archivo_cambios(pixels=[[...], [...]], filas=5, ancho=100, len_texto=200)

    Result:
        'cambios.txt' file with the selected pixels for each row.
    """
    total_pixeles_mensaje = len_texto + 8  # Total pixels needed, including a 8-pixel header
    output_dir = 'data\\output\\txt'
    file_path = os.path.join(output_dir, 'cambios.txt')
    with open(file_path, 'w') as cambios:
        # Write the first 88 pixels to the first line of the file
        cambios.write(f"{pixels[0][0:88]}\n")
        
        # Process the required rows
        for i in range(filas):
            if total_pixeles_mensaje > ancho:  # If there are more pixels to process than available in one row
                texto = pixels[i + 1][0:total_pixeles_mensaje]  # Take the necessary pixels from the current row
                total_pixeles_mensaje -= ancho  # Reduce the remaining total by the processed width
            else:
                texto = pixels[i + 1]  # Use all pixels from the current row
            cambios.write(str(texto))  # Write the pixels to the file
    print("[INFO] 'cambios.txt' file created successfully.")
