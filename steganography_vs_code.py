import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==========================
# LOAD IMAGE
# ==========================
image = cv2.imread('output.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# ==========================
# ENCODING FUNCTION
# ==========================
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode_image(image, secret_text):
    binary_secret = text_to_binary(secret_text) + '1111111111111110'  # EOF marker
    data_index = 0
    img = image.copy()
    rows, cols, _ = img.shape

    for row in range(rows):
        for col in range(cols):
            for channel in range(3):  # R, G, B
                if data_index < len(binary_secret):
                    img[row, col, channel] = (img[row, col, channel] & ~1) | int(binary_secret[data_index])
                    data_index += 1
                else:
                    return img
    return img

# ==========================
# ENCODE AND SAVE IMAGE
# ==========================
secret_message = "This is a hidden message!"
encoded_img = encode_image(image, secret_message)

plt.imshow(encoded_img)
plt.title("Encoded Image")
plt.axis('off')
plt.show()

# Save encoded image
encoded_bgr = cv2.cvtColor(encoded_img, cv2.COLOR_RGB2BGR)
cv2.imwrite("encoded_image.png", encoded_bgr)

# ==========================
# DECODING FUNCTION
# ==========================
def decode_image(image):
    binary_data = ''
    for row in image:
        for pixel in row:
            for channel in pixel:
                binary_data += str(channel & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ''
    for byte in all_bytes:
        if byte == '11111110':  # EOF
            break
        decoded_text += chr(int(byte, 2))
    return decoded_text

# ==========================
# LOAD AND DECODE MESSAGE
# ==========================
decoded_img = cv2.imread('encoded_image.png')
decoded_img = cv2.cvtColor(decoded_img, cv2.COLOR_BGR2RGB)
hidden_message = decode_image(decoded_img)

print("🔓 Hidden Message:", hidden_message)
