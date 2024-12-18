import time
import convertions
import processImg
import key
import manipulation
import createImg

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
binarys = convertions.color_to_bin(pixels, ancho, alto)

# Binary processing
indicadores = manipulation.separar_clave(binariPass)
binPassSep = manipulation.separar_contrasena(binariPass, keyLong)
pixelsClaveModificada = manipulation.manipular_indicadores(
    binarys, indicadores)
pixelsIndicadores = manipulation.crear_pixeles(pixelsClaveModificada)
pixelsIndicadoresDec = convertions.bin_to_dec(pixelsIndicadores)

# Pixel Password
binPassMod = manipulation.manipular_contrasena(binarys, binPassSep, ancho)
pixelsBinContra = manipulation.crear_pixeles(binPassMod)
pixelsBinDec = convertions.bin_to_dec(
    pixelsBinContra)  # Pixeles Contraseña Modificados
pixelsPassMod = pixelsIndicadoresDec + \
    pixelsBinDec  # Total Pixeles para Contraseña
pixels[0][0:88] = pixelsPassMod

# Text processing
textEncrypt = "Hola esto es una prueba para encriptar"
textToList = list(textEncrypt)
textASCII = convertions.convert_ascii(textToList)# Texto convertido en ASCII
textBin =  convertions.dec_to_bin(textASCII)# Texto convertido en binario

totalBitsText= len(textBin)*8# Total de bits
totalPixelsText= round(totalBitsText/3 +1/3)

#Create pixels
pixelModDec= manipulation.manipulacion_texto(pixels,textBin,totalPixelsText)
finalPixels= createImg.insertar_mensaje_en_pixeles(pixels,pixelModDec,totalPixelsText,pixelsIndicadoresDec,ancho,alto)

#Crear archivo cambios
totalFilas=round((totalPixelsText/ancho)+0.5)
key.crear_archivo_cambios(pixels,totalFilas,ancho,totalPixelsText)

#Create new Img
ImgMod= createImg.crear_imagen(pixels,img,ancho,alto)
ImgMod.save('IMG\\ImagenModificada.jpg')


print("---"*10)
print(f"[INFO] Contraseña en ASCII: {asciiPass}")
print(f"[INFO] Total de Pixels: {totalPixels}")
print(f"[INFO] Total de Caracteres por Fila: {len(pixels)*3//8}")
print(f"[INFO] Total de Filas de la imagen: {alto}")
print(f"[INFO] Total de Pixeles de la contraseña: {len(pixelsPassMod)}")
print("---"*10)
print(f"[INFO] Texto a encriptar: {textEncrypt}")
print(f"[INFO] Total de bits que usara el texto a encryptar: {totalBitsText}")
print(f"[INFO] Total de Pixeles que usara el texto a encryptar: {totalPixelsText}")

fin = time.time()
print(f"[INFO] Tiempo transcurrido: {round(fin - inicio,3)} seg")
