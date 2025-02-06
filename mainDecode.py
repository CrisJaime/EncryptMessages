import modules

# --- Load Modified Image ---
nameImgMod = "data\\output\\img\\ImagenModificada.jpg"
imgMod = modules.processImg.cargar_imagen(nameImgMod)
pixels, _, ancho, alto = modules.processImg.extraer_canales(imgMod)

# --- Extract Password ---
pixelsClaveExtraida = pixels[0][0:88]  # Extract the first 88 pixels
chunks = [pixelsClaveExtraida[i] for i in range(0, len(pixelsClaveExtraida))]
flatPixels = [value for sublist in chunks for value in sublist]
flatPixelsBin=modules.convertions.dec_to_bin(flatPixels)
lsbPixels= modules.manipulation.lsb_values(flatPixelsBin)
print(chunks)