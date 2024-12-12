import time
import convertions
import processImg
import key
import manipulation

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

# Binary processing
indicadores = manipulation.separar_clave(binariPass)
binPassSep = manipulation.separar_contrasena(binariPass,keyLong)
pixelsClaveModificada = manipulation.manipular_indicadores(binarys,indicadores)
pixelsIndicadores= manipulation.crear_pixeles(pixelsClaveModificada)
pixelsIndicadoresDec=convertions.bin_to_dec(pixelsIndicadores)

print(f"[INFO] Total de Caracteres por Fila: {len(pixels)*3//8}")
print(f"[INFO] Total de Filas de la imagen: {alto}")

fin = time.time()
print(f"[INFO] Tiempo transcurrido: {round(fin - inicio,3)} seg")