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
    
# Create a 'Llave.txt' file with a total of Pixels of the Text at the end
def final_password(password:str,totalPixelsText:int):
    extraChar='#'
    finalPass=password+extraChar+str(totalPixelsText)
    crear_archivo(finalPass)
    return finalPass