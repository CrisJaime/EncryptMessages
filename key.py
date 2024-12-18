import string
import random
from typing import List

# Generar una contraseña segura con letras, números y símbolos especiales
def crear_contrasena(n: int) -> str:
    """
    Genera una contraseña segura de longitud n, combinando letras, números y caracteres especiales.

    La contraseña siempre comienza con tres caracteres especiales ('@', '^', '#'), 
    seguidos por una combinación aleatoria de letras y números.

    Args:
        n (int): Longitud total de la contraseña generada.

    Returns:
        str: Contraseña generada aleatoriamente.

    Ejemplo:
        crear_contrasena(10) -> "@^#aB2cD3E4"
    """
    caracteres = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y dígitos
    contrasena = '@^#' + ''.join(random.choice(caracteres) for _ in range(n))  # Caracteres aleatorios
    print("[INFO] Se generó la contraseña correctamente.")
    return contrasena

# Crear un archivo 'Llave.txt' con una lista de líneas
def crear_archivo(contenido: List[str]) -> None:
    """
    Crea un archivo llamado 'Llave.txt' y escribe en él las líneas proporcionadas.

    Args:
        contenido (List[str]): Lista de líneas que se escribirán en el archivo.

    El archivo se guarda en la carpeta `Files`.

    Ejemplo:
        crear_archivo(["línea 1\n", "línea 2\n"])

    Resultado:
        Archivo 'Llave.txt' con el siguiente contenido:
        línea 1
        línea 2
    """
    with open('Files\\Llave.txt', 'w') as archivo:
        archivo.writelines(contenido)  # Escribe las líneas en el archivo
    print("[INFO] Se creó correctamente el archivo de la contraseña: 'Llave.txt'.")

# Crear un archivo 'cambios.txt' basado en los valores de píxeles y el tamaño del mensaje
def crear_archivo_cambios(pixels: List[List[int]], filas: int, ancho: int, len_texto: int) -> None:
    """
    Crea un archivo llamado 'cambios.txt' que contiene información sobre los píxeles modificados.

    Args:
        pixels (List[List[int]]): Lista bidimensional que representa los valores RGB de los píxeles.
        filas (int): Número de filas en la matriz de píxeles.
        ancho (int): Número de píxeles en cada fila (ancho de la imagen).
        len_texto (int): Longitud del mensaje que se procesará en píxeles.

    El archivo se guarda en la carpeta Files.

    Proceso:
    - Escribe la primera línea del archivo con los primeros 88 píxeles de la matriz.
    - Para las filas subsiguientes, incluye la cantidad necesaria de píxeles dependiendo 
      del tamaño restante del mensaje (len_texto + 8).

    Ejemplo:
        crear_archivo_cambios(pixels=[[...], [...]], filas=5, ancho=100, len_texto=200)

    Resultado:
        Archivo 'cambios.txt' con los píxeles seleccionados por cada fila.

    """
    total_pixeles_mensaje = len_texto + 8  # Total de píxeles necesarios, considerando un encabezado de 8
    with open('Files\\cambios.txt', 'w') as cambios:
        # Escribir los primeros 88 píxeles en la primera línea del archivo
        cambios.write(f"{pixels[0][0:88]}\n")
        
        # Procesar las filas necesarias
        for i in range(filas):
            if total_pixeles_mensaje > ancho:  # Si quedan más píxeles por procesar que los disponibles en una fila
                texto = pixels[i + 1][0:total_pixeles_mensaje]  # Tomar píxeles necesarios de la fila actual
                total_pixeles_mensaje -= ancho  # Reducir el total restante por el ancho procesado
            else:
                texto = pixels[i + 1]  # Usar todos los píxeles de la fila actual
            cambios.write(str(texto))  # Escribir los píxeles en el archivo
    print("[INFO] Se creó correctamente el archivo de los cambios: 'cambios.txt'.")