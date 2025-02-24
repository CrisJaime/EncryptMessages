import time  # Measure execution time
import modules  # Import custom modules for key handling, image processing, and conversions

# --- Start execution time measurement ---
start_time = time.time()

# --- Password Generation ---
KEY_LENGTH = 30  # Define password length
password = modules.key.crear_contrasena(KEY_LENGTH)  # Generate a random password
binary_password = modules.convertions.char_to_bin(password)  # Convert password to binary

# --- Image Processing ---
IMAGE_PATH = "data\input\img\ImageTest.jpg"  # Define image path
image = modules.processImg.cargar_imagen(IMAGE_PATH)  # Load the image
pixels, total_pixels, width, height = modules.processImg.extraer_canales(image)  # Extract RGB channels
binary_pixels = modules.convertions.color_to_bin(pixels, width, height)  # Convert RGB values to binary

# --- Binary Manipulation ---
key_indicators = modules.manipulation.separar_clave(binary_password)  # Extract key indicators
split_binary_password = modules.manipulation.separar_contrasena(binary_password, KEY_LENGTH)  # Split password
modified_key_pixels = modules.manipulation.manipular_indicadores(binary_pixels, key_indicators)  # Modify pixels
indicator_pixels = modules.manipulation.crear_pixeles(modified_key_pixels)  # Create pixels with indicators
indicator_pixels_dec = modules.convertions.bin_to_dec(indicator_pixels)  # Convert to decimal

# --- Embed Password into Image ---
modified_binary_password = modules.manipulation.manipular_contrasena(binary_pixels, split_binary_password, width)
password_pixels = modules.manipulation.crear_pixeles(modified_binary_password)
password_pixels_dec = modules.convertions.bin_to_dec(password_pixels)
pixels_password_modified = indicator_pixels_dec + password_pixels_dec  # Combine indicators and password
pixels[0][0:88] = pixels_password_modified  # Update first 88 pixels with password

# --- Process Text to Encrypt ---
with open('data/input/text/textEncrypt.txt', 'r', encoding='utf-8') as file:
    text_to_encrypt = file.read()  # Read text from file

text_list = list(text_to_encrypt)  # Convert text to list of characters
binary_text = modules.convertions.char_to_bin(text_list)  # Convert text to binary

# Calculate required storage space
total_text_bits = len(binary_text) * 8  # Total bits for text
required_pixels = round(total_text_bits / 3 + 1 / 3)  # Pixels needed

# --- Embed Text into Image ---
modified_pixels_dec = modules.manipulation.manipulacion_texto(pixels, binary_text, required_pixels)
pixels = modules.createImg.final_pixels(pixels, modified_pixels_dec, width)  # Update pixels

# --- Generate and Save Modified Image ---
modified_image = modules.createImg.crear_imagen(pixels, width, height)  # Create new image
modified_image.save('data\output\img\ImagenModificada.jpg')  # Save output image

# --- Generate Final Key ---
final_password = modules.key.final_password(password, required_pixels)  # Generate final password

# --- Output Information ---
print("---" * 10)
print(f"[INFO] Password in ASCII: {final_password}")
print(f"[INFO] Total pixels: {total_pixels}")
print(f"[INFO] Characters per row: {len(pixels) * 3 // 8}")
print(f"[INFO] Rows in image: {height}")
print(f"[INFO] Pixels used for password: {len(pixels_password_modified)}")
print("---" * 10)
print(f"[INFO] Text to encrypt: {text_to_encrypt}")
print(f"[INFO] Total bits used for text: {total_text_bits}")
print(f"[INFO] Total pixels used for text: {required_pixels}")

# --- End execution time measurement ---
end_time = time.time()
print(f"[INFO] Time elapsed: {round(end_time - start_time, 3)} sec")
