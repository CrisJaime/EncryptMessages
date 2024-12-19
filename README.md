# Image Encryption Project

This project focuses on encrypting text into an image using a series of image processing techniques, including binary manipulation, password generation, and encoding. The main goal is to hide a secret message inside an image using pixel manipulation while also securing the message with a password.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Modules](#modules)
   - [Key Generation](#key-generation)
   - [Image Processing](#image-processing)
   - [Binary Manipulation](#binary-manipulation)
   - [Image Creation](#image-creation)
3. [How to Use](#how-to-use)
4. [File Structure](#file-structure)
5. [Requirements](#requirements)

## Project Overview

This project uses various techniques to hide encrypted messages in image files. It works by manipulating the image pixels based on a password and a message to be encrypted. The process includes:
- **Password Generation**: Generates a random password and stores it in a file.
- **Image Processing**: Loads an image, extracts its RGB values, and converts them into binary.
- **Binary Manipulation**: Uses the binary password and message to modify the image's pixels.
- **Text Encryption**: Encrypts the provided message by converting it to binary and embedding it into the image.
- **Image Creation**: After modifying the pixels, a new image is created and saved with the encrypted message embedded.

## Modules

### Key Generation
The `key` module handles the creation of a password for encrypting the text. The password is generated randomly, converted into ASCII values, and then into binary form.

### Image Processing
The `processImg` module is responsible for loading and processing images. It extracts RGB channels from the image and converts them into a binary representation that can be manipulated.

### Binary Manipulation
The `manipulation` module manipulates the binary data representing the password and message. It modifies the image's pixels by encoding the binary data (indicators, password, and message) into the image's pixel values.

### Image Creation
The `createImg` module manages inserting the encrypted message and password into the image. It updates the pixel data of the image with the binary data of the message and password, then creates a new image with the modified pixel values.

## How to Use

1. **Generate a Password**:
   - The program generates a random password of a specified length.
   - The password is saved to a file and also converted to ASCII and binary formats.

2. **Encrypt an Image**:
   - Load the image you want to encrypt.
   - Extract the image’s RGB channels.
   - Convert the image's RGB values to binary.
   - Embed the password and the message you want to encrypt into the image pixels.

3. **Save the Modified Image**:
   - After embedding the message and password into the image pixels, a new image is created and saved to a file.

4. **Text Encryption**:
   - The text to be encrypted is converted into binary and embedded into the image's pixel values.

## File Structure
Here's the file structure of the project:

```
project_directory/
│
├── data/
│   ├── input/
│   │   └── img/
│   │       └── ImageTest.jpg        # Input image 
│   │   └── text/
│   │       └── inputText.txt        # Input text
file
│   ├── output/
│   │   └── img/
│   │       └── ImagenModificada.jpg # Output 
│   │   └── txt/
│   │       └── cambios.txt          # Pixels Changes
│   │       └── key.txt              # Key/Password
modified image
│
├── modules/
│   ├── convertions.py               # Helper functions for conversions (binary, decimal, ASCII, etc.)
│   ├── processImg.py                # Functions for image processing
│   ├── key.py                       # Functions for password generation and saving
│   ├── manipulation.py              # Functions for binary manipulation
│   └── createImg.py                 # Functions for creating the final modified image
│
├── mainEncrypt.py                   # Main script to run the encryption process
└── README.md                        # Project documentation (this file)
```

## Requirements

- Python 3.x
- PIL (Pillow)
- Custom modules (`convertions`, `processImg`, `key`, `manipulation`, `createImg`)

To install the required Python libraries, use:

```bash
pip install Pillow
