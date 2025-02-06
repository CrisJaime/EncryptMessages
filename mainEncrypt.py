import time  # To measure execution time
import modules

# Measure the start time of the program
inicio = time.time()

# --- Password Generation ---
keyLong = 30  # Length of the password
password = modules.key.crear_contrasena(keyLong)  # Create password with random characters
keyFile = modules.key.crear_archivo(password)  # Save the password in a text file
binariPass=modules.convertions.char_to_bin(password)

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
print(f"[INFO] First 8 pixels after password indicators: \n{pixelsIndicadoresDec}")
# --- Insert Password into the Image ---

# --- Output Information ---