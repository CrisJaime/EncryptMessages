import time
import key

from PIL import Image


inicio = time.time()

keyLong=30
password= key.crear_contrasena(keyLong)
keyFile= key.crear_archivo(password)

fin = time.time()
print(f"[INFO] Tiempo transcurrido: {round(fin - inicio,3)} seg")