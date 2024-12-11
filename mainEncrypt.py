import time
import convertions
import processImg
import key

inicio = time.time()

keyLong = 30
password = key.crear_contrasena(keyLong)
keyFile = key.crear_archivo(password)
asciiPass = convertions.convert_ascii(password)
binariPass = convertions.dec_to_bin(asciiPass)

# Img Processing
nameImg = "IMG\ImageTest.jpg"
img = processImg.cargar_imagen(nameImg)
pixels, totalPixels, ancho, alto = processImg.extraer_canales(img)
binarys= convertions.color_to_bin(pixels,ancho,alto)

print(f"[INFO] ASCII: {asciiPass}")
print(f"[INFO] Total de Pixels: {totalPixels}")

fin = time.time()
print(f"[INFO] Tiempo transcurrido: {round(fin - inicio,3)} seg")