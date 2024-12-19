from PIL import Image
import sys

# Function to load an image
def cargar_imagen(nombre_archivo: str):
    """
    Loads an image from a file and handles errors if the file is not found.

    Args:
        nombre_archivo (str): Name of the image file (with extension).

    Returns:
        Image.Image: Loaded image object if the file is found.

    Error Handling:
        - If the file does not exist, an error message is displayed, and the program exits.

    Example:
        cargar_imagen('image.jpg') -> Loads and returns the image in PIL.Image format.
    """
    try:
        imagen = Image.open(nombre_archivo)  # Opens the image file
        print(f"[INFO] Image loaded successfully: {imagen.format}, Size: {imagen.size}, Mode: {imagen.mode}")
        return imagen
    except FileNotFoundError:
        print(f'No image found with the name "{nombre_archivo}".')  # Error handling if the file is not found
        sys.exit(1)  # Exits the program with an error code

# Extract RGB channels from an image
def extraer_canales(imagen: Image.Image):
    """
    Extracts the RGB channels of each pixel in the image and organizes the values into a matrix.

    Args:
        imagen (Image.Image): Loaded image object in PIL format.

    Returns:
        tuple:
            - matrix (list): Three-dimensional matrix containing RGB values for each pixel.
            - total_pixels (int): Total number of pixels in the image.
            - width (int): Image width in pixels.
            - height (int): Image height in pixels.

    Example:
        extraer_canales(image) ->
        matrix = [[[R1, G1, B1], [R2, G2, B2], ...], ...]
        total_pixels = width * height
    """
    width, height = imagen.size  # Get the image's width and height
    image_pixels = imagen.load()  # Load the image pixels into memory

    # Create a three-dimensional matrix with the RGB values of each pixel
    matrix = [
        [[*image_pixels[x, y]] for x in range(width)]  # Extract [R, G, B] for each pixel in the width
        for y in range(height)  # Iterate through each row (image height)
    ]
    total_pixels = width * height  # Calculate the total number of pixels
    return matrix, total_pixels, width, height

# Create and display a new image from processed pixels
def crear_imagen(pixels, imagen_original: Image.Image, ancho: int, alto: int, conversiones):
    """
    Creates a new image using processed pixel values and displays it alongside the original image.

    Args:
        pixels (list): List of processed RGB values.
        imagen_original (Image.Image): Original image object.
        ancho (int): Image width in pixels.
        alto (int): Image height in pixels.
        conversiones (module): Module with the convertToDuple function to convert pixels into tuples.

    Returns:
        Image.Image: New image created from the provided pixel values.

    Process:
        - Converts the list of pixels into a list of tuples (format [R, G, B]).
        - Creates a new image with the same size and applies the new pixels.
        - Displays both the new image and the original image.

    Example:
        new_image = crear_imagen(pixels, image, 200, 300, conversiones)
    """
    # Convert the list of pixels into RGB tuples using the convertToDuple function from the 'conversiones' module
    pixels_tuples = conversiones.convertToDuple(pixels, ancho, alto)
    
    # Create a new image in RGB mode with the specified dimensions
    new_image = Image.new('RGB', (ancho, alto))
    new_image.putdata(pixels_tuples)  # Place the processed pixels into the new image
    
    # Display the images: the new image and the original image
    new_image.show()
    imagen_original.show()
    
    return new_image
