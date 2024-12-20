from PIL import Image
import time
import modules


def read_file(file_path, error_message):
    """
    Reads a file and returns its content as a string.
    Exits the program if the file is not found.

    Args:
        file_path (str): Path to the file.
        error_message (str): Error message to display if the file is not found.

    Returns:
        str: Content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(error_message)
        exit()


def process_password_changes(contrasena):
    """
    Processes the password changes and verifies the correctness of the password.

    Args:
        contrasena (str): Password changes as a string.
    """
    # Convert password string to pixels
    recovered_pixels = modules.stego_utils.convert_password(contrasena)
    # Convert pixel values to binary
    pixel_bin = modules.stego_utils.decimal_to_binary(recovered_pixels)
    # Extract the binary password from pixel data
    password_bin = modules.stego_utils.extract_password_binary(pixel_bin)
    # Decode the password
    final_password = modules.stego_utils.reconstruct_password(password_bin)
    # Verify the password
    modules.stego_utils.validate_password(final_password)


def process_hidden_text(texto):
    """
    Processes the hidden text and prints the decoded message.

    Args:
        texto (str): Hidden text as a string.
    """
    # Convert text string to pixels
    text_pixels = modules.stego_utils.convert_password(texto)
    # Convert pixel values to binary
    text_bin = modules.stego_utils.decimal_to_binary(text_pixels)
    # Extract binary text data
    hidden_text_bin = modules.stego_utils.extract_password_binary(text_bin)
    # Decode the hidden text
    final_text = modules.stego_utils.decode_text(hidden_text_bin)
    # Print the decoded message
    modules.stego_utils.print_message(final_text)


def main():
    start_time = time.time()

    # Load the key file
    key_content = read_file(
        'data/output/txt/key.txt',
        '[INFO] The file "key.txt" is missing. Please provide a valid key file.'
    )
    print('[INFO] Key file loaded successfully.')

    # Load the changes file
    changes_content = read_file(
        'data/output/txt/cambios.txt',
        '[INFO] The file "cambios.txt" is missing. Please provide a valid changes file.'
    )
    print('[INFO] Changes file loaded successfully.')

    # Load the encoded image
    try:
        encoded_image = Image.open('data\output\img\ImagenModificada.jpg')
        print('[INFO] Encoded image loaded successfully.')
        # Optionally display the image
        # encoded_image.show()
    except FileNotFoundError:
        print(
            '[INFO] The file "ImagenModificada.jpg" is missing. Please provide the encoded image.')
        exit()

    # Process the password and hidden text
    changes_lines = changes_content.splitlines()
    if len(changes_lines) < 2:
        print('[ERROR] Invalid changes file format.')
        exit()

    password_changes = changes_lines[0]
    hidden_text_changes = changes_lines[1]

    # Process password
    process_password_changes(password_changes)

    # # Process hidden text
    # process_hidden_text(hidden_text_changes)

    # Measure execution time
    end_time = time.time()
    print(f'[INFO] Execution time: {round(end_time - start_time, 3)} seconds')


if __name__ == '__main__':
    main()
