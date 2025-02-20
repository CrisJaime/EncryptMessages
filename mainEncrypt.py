import time  # To measure execution time
import modules  # Import custom modules for handling keys, images, and conversions

# --- Measure program start time ---
inicio = time.time()

# --- Password Generation ---
keyLong = 30  # Password length
# Create a random password with characters
password = modules.key.crear_contrasena(keyLong)
# Save the password in a text file
keyFile = modules.key.crear_archivo(password)
# Convert the password to binary
binariPass = modules.convertions.char_to_bin(password)

# --- Image Processing ---
nameImg = "data\\input\\img\\ImageTest.jpg"  # Path of the original image
# Load the image from the file
img = modules.processImg.cargar_imagen(nameImg)
# Extract RGB channels and get image dimensions
pixels, totalPixels, ancho, alto = modules.processImg.extraer_canales(img)
# Convert RGB color values to binary
binarys = modules.convertions.color_to_bin(pixels, ancho, alto)

# --- Binary Manipulation ---
# Separate key indicators from the binary password
indicadores = modules.manipulation.separar_clave(binariPass)
# Split the binary password according to the specified length
binPassSep = modules.manipulation.separar_contrasena(binariPass, keyLong)
# Modify pixels with key indicators
pixelsClaveModificada = modules.manipulation.manipular_indicadores(binarys, indicadores)
# Create pixels with modified indicators
pixelsIndicadores = modules.manipulation.crear_pixeles(pixelsClaveModificada)
# Convert indicator pixels from binary to decimal
pixelsIndicadoresDec = modules.convertions.bin_to_dec(pixelsIndicadores)

# --- Insert Password into the Image ---
# Modify pixels with the binary password
binPassMod = modules.manipulation.manipular_contrasena(binarys, binPassSep, ancho)
# Create pixels with the modified password
pixelsBinContra = modules.manipulation.crear_pixeles(binPassMod)
# Convert password pixels from binary to decimal
pixelsBinDec = modules.convertions.bin_to_dec(pixelsBinContra)
# Combine indicator pixels with password pixels
pixelsPassMod = pixelsIndicadoresDec + pixelsBinDec
# Update the first 88 pixels with the password in the image
pixels[0][0:88] = pixelsPassMod

# --- Process Text to Encrypt ---
# Read text to encrypt from a file
with open('data/input/text/textEncrypt.txt', 'r', encoding='utf-8') as file:
    textEncrypt = file.read()
# Convert the text into a list of characters
textToList = list(textEncrypt)
# Convert characters to binary
textBin = modules.convertions.char_to_bin(textToList)
# Calculate the total number of bits of the text
totalBitsText = len(textBin) * 8
# Calculate the total number of pixels required to store the text
totalPixelsText = round(totalBitsText / 3 + 1 / 3)

# --- Create Modified Pixels with the Text ---
# Modify pixels to include the encrypted text
pixelModDec = modules.manipulation.manipulacion_texto(pixels, textBin, totalPixelsText)
# Generate the final image with modified pixels
pixels = modules.createImg.final_pixels(pixels, pixelModDec, ancho)

# --- Create Modified Image ---
# Create a new image with modified pixels
imgMod = modules.createImg.crear_imagen(pixels, ancho, alto)
# Save the modified image to a file
imgMod.save('data\\output\\img\\ImagenModificada.jpg')

# --- Output Information ---
print("---" * 10)
print(f"[INFO] Password in ASCII: {password}")
print(f"[INFO] Total pixels: {totalPixels}")
print(f"[INFO] Characters per row: {len(pixels) * 3 // 8}")
print(f"[INFO] Rows in the image: {alto}")
print(f"[INFO] Pixels of the password: {len(pixelsPassMod)}")
print("---" * 10)
print(f"[INFO] Text to encrypt: {textEncrypt}")
print(f"[INFO] Total bits the text will use: {totalBitsText}")
print(f"[INFO] Total pixels the text will use: {totalPixelsText}")

# --- Measure execution time ---
fin = time.time()
print(f"[INFO] Time elapsed: {round(fin - inicio, 3)} sec")
