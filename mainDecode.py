import modules

# --- Load Modified Image ---
nameImgMod = "data\\output\\img\\ImagenModificada.jpg"
imgMod = modules.processImg.cargar_imagen(nameImgMod)
pixels, _, ancho, alto = modules.processImg.extraer_canales(imgMod)

# --- Password ---
with open("data\\output\\txt\\key.txt", 'r', encoding='utf-8') as passFull:
    password = passFull.read() 
passDivide=modules.key.separate_password(password)
indicatorsPass=modules.convertions.char_to_bin(passDivide[0])
passwordBin=modules.convertions.char_to_bin(passDivide[1])
rows=passDivide[2]

