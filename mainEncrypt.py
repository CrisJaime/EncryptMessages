import time  # To measure execution time
import modules

# Measure the start time of the program
inicio = time.time()

# --- Password Generation ---
keyLong = 30  # Length of the password
# Create password with random characters
password = modules.key.crear_contrasena(keyLong)
# Save the password in a text file
keyFile = modules.key.crear_archivo(password)
binariPass = modules.convertions.char_to_bin(password)

# --- Image Processing ---
nameImg = "data\\input\\img\\ImageTest.jpg"  # Path of the original image
img = modules.processImg.cargar_imagen(nameImg)  # Load the image from the file
pixels, totalPixels, ancho, alto = modules.processImg.extraer_canales(
    img)  # Extract RGB channels and get dimensions
binarys = modules.convertions.color_to_bin(
    pixels, ancho, alto)  # Convert RGB color values to binary

# --- Binary Manipulation ---
indicadores = modules.manipulation.separar_clave(
    binariPass)  # Split the key indicators
binPassSep = modules.manipulation.separar_contrasena(
    binariPass, keyLong)  # Split the binary password
pixelsClaveModificada = modules.manipulation.manipular_indicadores(
    binarys, indicadores)  # Modify pixels with indicators
pixelsIndicadores = modules.manipulation.crear_pixeles(
    pixelsClaveModificada)  # Create pixels with modified indicators
pixelsIndicadoresDec = modules.convertions.bin_to_dec(
    pixelsIndicadores)  # Convert indicator pixels to decimal
print(
    f"[INFO] First 8 pixels after password indicators: \n{pixelsIndicadoresDec}")

# --- Insert Password into the Image ---
binPassMod = modules.manipulation.manipular_contrasena(
    binarys, binPassSep, ancho)  # Modify pixels with the binary password
pixelsBinContra = modules.manipulation.crear_pixeles(
    binPassMod)  # Create pixels with modified password
# Convert modified password pixels to decimal
pixelsBinDec = modules.convertions.bin_to_dec(pixelsBinContra)
# Combine indicator pixels and password pixels
pixelsPassMod = pixelsIndicadoresDec + pixelsBinDec
pixels[0][0:88] = pixelsPassMod  # Update the first 88 pixels with the password

# --- Process Text to Encrypt ---
textEncrypt = "Una mañana, al despertar de un sueño agitado, Gregorio Samsa se encontró en su cama convertido en un insecto monstruoso. Estaba acostado sobre su espalda dura como un caparazón y, al levantar un poco la cabeza, vio su vientre convexo y oscuro, surcado por curvadas estrías, sobre el cual apenas se sostenía la colcha, a punto de resbalar del todo. Sus numerosas patas, ridículamente pequeñas en comparación con el resto de su cuerpo, se agitaban sin concierto.Al intentar darse la vuelta sobre el costado, lo cual era su postura habitual para dormir, notó que no podía hacerlo. Por mucho que se esforzara, siempre volvía a quedar boca arriba. Probó hacerlo cientos de veces, cerrando los ojos para no ver sus patas agitándose, y solo desistió cuando sintió un leve dolor en el costado, nunca antes experimentado.Fuera, la lluvia golpeaba con fuerza los cristales de la ventana. '¿Qué pasaría si siguiera durmiendo un poco más y me olvidara de todas estas tonterías?', pensó. Pero era algo completamente imposible, ya que estaba acostumbrado a dormir del lado derecho y, en su estado actual, no podía adoptar esa postura.Al otro lado de la puerta, Gregorio escuchó cómo su padre ya comenzaba a impacientarse. ‘Gregorio’, llamó su madre con voz suave, ‘el tren sale dentro de poco’. Pero él no podía responder. Sentía su boca seca y torpe, su lengua incapaz de articular las palabras que antes le salían con tanta naturalidad. Todo en su cuerpo era extraño, ajeno, como si su propia existencia le hubiera sido arrebatada de un día para otro."  # Text to encrypt
textToList = list(textEncrypt)  # Convert the text into a list of characters
textBin = modules.convertions.char_to_bin(
    textToList)  # Convert characters to binary
totalBitsText = len(textBin) * 8  # Calculate the total bits of the text
# Calculate the total pixels required for the text
totalPixelsText = round(totalBitsText / 3 + 1 / 3)

# --- Create Modified Pixels with the Text ---
pixelModDec = modules.manipulation.manipulacion_texto(
    pixels, textBin, totalPixelsText)  # Modify pixels with the text
print(
    f"[INFO] Total of pixels for the modify text: {len(pixelModDec)} pixels")
pixels=modules.createImg.final_pixels(pixels,pixelModDec,ancho)

# --- Output Information ---
