# Image Steganography using Python

##  Project Overview

This project demonstrates image steganography using Python.

Steganography is a technique used to hide secret information inside another file, such as an image, without making the hidden information visibly noticeable.

In this project, a secret text message is hidden inside an image using the Least Significant Bit (LSB) technique.

## Objective

The main objective of this project is to:

- Hide a secret text message inside an image
- Extract the hidden message from the encoded image
- Understand the basic working of LSB-based image steganography

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib

##  How It Works

### 1. Load Image

The input image is loaded using OpenCV.

### 2. Convert Text to Binary

The secret message is converted into binary format.

### 3. Encode Message

The binary message is stored in the Least Significant Bits (LSB) of the image pixels.

### 4. Save Encoded Image

The modified image is saved as:

```text
encoded_image.png

5. Decode Message

The program reads the Least Significant Bits from the encoded image and reconstructs the original hidden message.

## Project Structure
Image-Steganography/
│
├── steganography_vs_code.py
├── output.png
├── encoded_image.png
└── README.md
🔐 Example

The program hides the following message:

This is a hidden message!

After decoding, the program displays:

🔓 Hidden Message: This is a hidden message!
📊 Output

##The program displays:
-Original image
-Encoded image
-Decoded hidden message

##Future Improvements
-Add a Streamlit web interface
-Allow users to enter their own secret message
-Allow users to upload their own image
-Add password-based encryption
-Improve error handling and message capacity

##Author
Sonam Kumari
