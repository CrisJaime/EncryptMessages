import string
import random
from typing import List

# Generar una contraseña segura con letras, números y símbolos especiales
def crear_contrasena(n: int) -> str:
    """
    Genera una contraseña de longitud n con letras, números y caracteres especiales al inicio.
    """
    caracteres = string.ascii_letters + string.digits
    contrasena = '@^#' + ''.join(random.choice(caracteres) for _ in range(n))
    print("[INFO] Se generó la contraseña correctamente.")
    return contrasena

# Crear un archivo 'Llave.txt' con una lista de líneas
def crear_archivo(contenido: List[str]) -> None:
    """
    Crea un archivo 'Llave.txt' escribiendo las líneas proporcionadas.
    """
    with open('Files\Llave.txt', 'w') as archivo:
        archivo.writelines(contenido)
    print("[INFO] Se creó correctamente el archivo de la contraseña: 'Llave.txt'.")

# Crear un archivo 'cambios.txt' basado en los valores de píxeles y el tamaño del mensaje
def crear_archivo_cambios(pixels: List[List[int]], filas: int, ancho: int, len_texto: int) -> None:
    """
    Crea un archivo 'cambios.txt' escribiendo información basada en los píxeles.
    """
    total_pixeles_mensaje = len_texto + 8
    with open('Files\cambios.txt', 'w') as cambios:
        # Primera línea del archivo con los primeros 88 píxeles
        cambios.write(f"{pixels[0][0:88]}\n")
        
        for i in range(filas):
            if total_pixeles_mensaje > ancho:
                texto = pixels[i + 1][0:total_pixeles_mensaje]
                total_pixeles_mensaje -= ancho
            else:
                texto = pixels[i + 1]
            cambios.write(str(texto))
    print("[INFO] Se creó correctamente el archivo de los cambios: 'cambios.txt'.")