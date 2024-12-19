import time  # To measure execution time
import modules

# Measure the start time of the program
inicio = time.time()

# --- Password Generation ---
keyLong = 30  # Length of the password
password = modules.key.crear_contrasena(keyLong)  # Create password with random characters
keyFile = modules.key.crear_archivo(password)  # Save the password in a text file
asciiPass = modules.convertions.convert_ascii(password)  # Convert the password to ASCII values
binariPass = modules.convertions.dec_to_bin(asciiPass)  # Convert ASCII values to binary

# --- Image Processing ---
nameImg = "data\\input\\img\\ImageTest.jpg"  # Path of the original image
img = modules.processImg.cargar_imagen(nameImg)  # Load the image from the file
pixels, totalPixels, ancho, alto = modules.processImg.extraer_canales(img)  # Extract RGB channels and get dimensions
binarys = modules.convertions.color_to_bin(pixels, ancho, alto)  # Convert RGB color values to binary

# --- Binary Manipulation ---
indicadores = modules.manipulation.separar_clave(binariPass)  # Split the key indicators
binPassSep = modules.manipulation.separar_contrasena(binariPass, keyLong)  # Split the binary password
pixelsClaveModificada = modules.manipulation.manipular_indicadores(binarys, indicadores)  # Modify pixels with indicators
pixelsIndicadores = modules.manipulation.crear_pixeles(pixelsClaveModificada)  # Create pixels with modified indicators
pixelsIndicadoresDec = modules.convertions.bin_to_dec(pixelsIndicadores)  # Convert indicator pixels to decimal

# --- Insert Password into the Image ---
binPassMod = modules.manipulation.manipular_contrasena(binarys, binPassSep, ancho)  # Modify pixels with the binary password
pixelsBinContra = modules.manipulation.crear_pixeles(binPassMod)  # Create pixels with modified password
pixelsBinDec = modules.convertions.bin_to_dec(pixelsBinContra)  # Convert modified password pixels to decimal
pixelsPassMod = pixelsIndicadoresDec + pixelsBinDec  # Combine indicator pixels and password pixels
pixels[0][0:88] = pixelsPassMod  # Update the first 88 pixels with the password

# --- Process Text to Encrypt ---
textEncrypt = "Hola esto es una prueba para encriptar"  # Text to encrypt
textToList = list(textEncrypt)  # Convert the text into a list of characters
textASCII = modules.convertions.convert_ascii(textToList)  # Convert characters to ASCII
textBin = modules.convertions.dec_to_bin(textASCII)  # Convert ASCII values to binary

totalBitsText = len(textBin) * 8  # Calculate the total bits of the text
totalPixelsText = round(totalBitsText / 3 + 1 / 3)  # Calculate the total pixels required for the text

# --- Create Modified Pixels with the Text ---
pixelModDec = modules.manipulation.manipulacion_texto(pixels, textBin, totalPixelsText)  # Modify pixels with the text
finalPixels = modules.createImg.insertar_mensaje_en_pixeles(  # Insert the message into the image pixels
    pixels, pixelModDec, totalPixelsText, pixelsIndicadoresDec, ancho, alto
)

# --- Create File with Changes Made ---
totalFilas = round((totalPixelsText / ancho) + 0.5)  # Calculate the total affected rows
modules.key.crear_archivo_cambios(pixels, totalFilas, ancho, totalPixelsText)  # Save changes in a file

# --- Create Modified Image ---
ImgMod = modules.createImg.crear_imagen(pixels, img, ancho, alto)  # Create a new image with modified pixels
ImgMod.save('data\\output\\img\\ImagenModificada.jpg')  # Save the modified image to a file

# --- Output Information ---
print("---" * 10)
print(f"[INFO] Password in ASCII: {asciiPass}")
print(f"[INFO] Total Pixels: {totalPixels}")
print(f"[INFO] Total Characters per Row: {len(pixels)*3//8}")
print(f"[INFO] Total Rows in the image: {alto}")
print(f"[INFO] Total Pixels of the Password: {len(pixelsPassMod)}")
print("---" * 10)
print(f"[INFO] Text to encrypt: {textEncrypt}")
print(f"[INFO] Total bits the text to encrypt will use: {totalBitsText}")
print(f"[INFO] Total Pixels the text to encrypt will use: {totalPixelsText}")

# Measure the end time and calculate the duration
fin = time.time()
print(f"[INFO] Time elapsed: {round(fin - inicio, 3)} sec")
