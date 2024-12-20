# Cache for storing binary conversions of colors
color_to_bin_cache = {}

def convert_password(data):
    """
    Converts a raw password array into a list of RGB pixel values.
    
    Args:
        data (list): A list containing characters of the password.
    
    Returns:
        list: A list of RGB pixel values as [R, G, B].
    """
    filtered_data = [
        char for char in data if str.isdigit(char) or char not in [' ', '[', ']']
    ][:-1]  # Remove trailing unwanted characters

    numeric_values = []
    temp_digits = []

    for char in filtered_data:
        if str.isdigit(char):
            temp_digits.append(char)
        else:
            if temp_digits:
                numeric_values.append(int(''.join(temp_digits)))
                temp_digits.clear()
    
    # Handle remaining digits
    if temp_digits:
        numeric_values.append(int(''.join(temp_digits)))

    # Create RGB triplets
    total_pixels = len(numeric_values) // 3
    pixels = [
        [numeric_values[i], numeric_values[i + 1], numeric_values[i + 2]]
        for i in range(0, total_pixels * 3, 3)
    ]
    return pixels

def decimal_to_binary(pixels):
    """
    Converts a list of RGB pixel values to binary format.
    
    Args:
        pixels (list): A list of RGB pixel values as [R, G, B].
    
    Returns:
        list: A list of RGB pixel values in binary format.
    """
    binary_pixels = []

    for r, g, b in pixels:
        rb = color_to_bin_cache.get(r, list(format(r, '08b')))
        gb = color_to_bin_cache.get(g, list(format(g, '08b')))
        bb = color_to_bin_cache.get(b, list(format(b, '08b')))

        color_to_bin_cache[r] = rb
        color_to_bin_cache[g] = gb
        color_to_bin_cache[b] = bb

        binary_pixels.append([rb, gb, bb])

    return binary_pixels

def extract_password_binary(binary_pixels):
    """
    Extracts the binary password from the least significant bits of the binary pixel values.
    
    Args:
        binary_pixels (list): A list of RGB pixel values in binary format.
    
    Returns:
        list: A list of binary values representing the password.
    """
    password_binary = []
    for r, g, b in binary_pixels:
        password_binary.extend([int(r[7]), int(g[7]), int(b[7])])
    return password_binary

def reconstruct_password(binary_password):
    """
    Converts a binary password back to its character representation.
    
    Args:
        binary_password (list): A list of binary values representing the password.
    
    Returns:
        list: A list of characters representing the password.
    """
    return [
        chr(int(''.join(map(str, binary_password[i:i + 8])), 2))
        for i in range(0, len(binary_password), 8)
    ]

def decode_text(encoded_binary):
    """
    Decodes the hidden message from the binary representation.
    
    Args:
        encoded_binary (list): A list of binary values containing the encoded message.
    
    Returns:
        str: The decoded text message if the message contains valid delimiters.
    """
    delimiter = encoded_binary[-24:]
    message_binary = encoded_binary[:-24]

    decoded_delimiter = ''.join(
        chr(int(''.join(map(str, delimiter[i:i + 8])), 2))
        for i in range(0, len(delimiter), 8)
    )

    if decoded_delimiter == '@^#':
        return ''.join(reconstruct_password(message_binary))
    else:
        raise ValueError("No hidden message found.")

def validate_password(password):
    """
    Validates the password against the expected format.
    
    Args:
        password (list): A list of characters representing the password.
    """
    if password[:3] == ['@', '^', '#']:
        print("[INFO] Password is valid. Extracted password: ", ''.join(password[3:]))
    else:
        print("[INFO] Invalid password format.")

def print_message(message):
    """
    Prints the decoded message.
    
    Args:
        message (str): The decoded message to print.
    """
    print(f"[INFO] Decoded message: {message}")
