# Modules

## 1. **`convertions.py`**
This module contains various utility functions to handle data conversions. It is used to convert text to ASCII values, ASCII to binary, and vice versa. These functions are essential for the encryption and steganography processes as they ensure that the data can be embedded in the image.

- **`convert_ascii(data)`**: Converts a list of characters into their corresponding ASCII values.
- **`dec_to_bin(data)`**: Converts a list of decimal values to binary.
- **`bin_to_dec(data)`**: Converts binary values to decimal.
- **`color_to_bin(pixels, width, height)`**: Converts RGB color values from the image pixels into binary format for further processing.

## 2. **`processImg.py`**
This module is responsible for handling image-related operations. It includes functions to load an image, extract its RGB channels, and perform pixel manipulations.

- **`cargar_imagen(image_path)`**: Loads an image from the given file path.
- **`extraer_canales(image)`**: Extracts the RGB channels of the image and returns the pixel data, total pixels, and dimensions (width and height).
- **`extraer_canales(image)`**: Extracts the RGB values and returns them in a two-dimensional matrix.

## 3. **`key.py`**
This module handles password generation and storage. It includes functions to create random passwords, save them to a file, and generate changes for the encryption process.

- **`crear_contrasena(length)`**: Generates a random password of the specified length.
- **`crear_archivo(password)`**: Saves the generated password to a text file.
- **`crear_archivo_cambios(pixels, total_rows, width, total_pixels_text)`**: Saves changes made to the image pixels in a separate file for reference.

## 4. **`manipulation.py`**
This module contains the core logic for manipulating binary data and image pixels to embed the encrypted message and password into the image.

- **`separar_clave(binary_password)`**: Separates the binary password into indicators used for pixel manipulation.
- **`separar_contrasena(binary_password, key_length)`**: Separates the binary password into sections based on the password length.
- **`manipular_indicadores(binary_pixels, indicators)`**: Modifies the image pixels with the password indicators.
- **`crear_pixeles(modified_pixels)`**: Creates pixel values with modified data (binary password or indicators).
- **`manipular_contrasena(binary_pixels, binary_password, width)`**: Modifies the image pixels to encode the binary password.
- **`manipulacion_texto(pixels, binary_text, total_pixels_text)`**: Modifies the image pixels to encode the binary text message.

## 5. **`createImg.py`**
This module is responsible for creating the final modified image by embedding both the encrypted message and the password. It includes functions to insert messages into the image's pixels and create the final image file.

- **`insertar_mensaje_en_pixeles(pixels, binary_message, total_pixels_message, binary_indicators, width, height)`**: Inserts the binary message into the image pixels, appending indicators at the end of the message.
- **`open_image(image_path)`**: Opens an image from the provided file path and displays its properties.
- **`extraer_canales(image)`**: Extracts the RGB values from the image and returns them in a matrix format.
- **`crear_imagen(pixels, original_image, width, height)`**: Creates a new image using the modified pixel data, then displays the original and modified images.

# How It Works

1. **Password Generation**: A random password is generated and converted into binary format.
2. **Image Processing**: An image is loaded, and its pixels are extracted. The RGB values are then converted into binary for further manipulation.
3. **Binary Manipulation**: The binary password and binary message are embedded into the image using a set of indicators and modified pixels. The data is embedded into the image pixels in such a way that it can be extracted later.
4. **Image Creation**: The modified pixels are used to create a new image that contains the encrypted text and password hidden within it.
5. **File Saving**: The new image is saved, and the changes made to the pixels are recorded for future use.
