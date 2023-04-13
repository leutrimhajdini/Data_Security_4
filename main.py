from PIL import Image
import random

# Defining the color mapping for characters
color_map = {
    'A': (18, 48, 23),
    'B': (146, 182, 56),
    'C': (75, 1, 214),
    'D': (123, 168, 132),
    'E': (20, 116, 150),
    'F': (94, 224, 168),
    'G': (104, 132, 111),
    'H': (142, 108, 252),
    'I': (50, 117, 52),
    'J': (104, 79, 7),
    'K': (1, 32, 100),
    'L': (4, 129, 143),
    'M': (83, 95, 67),
    'N': (71, 66, 159),
    'O': (80, 12, 127),
    'P': (189, 55, 128),
    'Q': (9, 8, 173),
    'R': (216, 205, 77),
    'S': (102, 8, 249),
    'T': (215, 143, 131),
    'U': (128, 227, 228),
    'V': (197, 211, 114),
    'W': (186, 76, 132),
    'X': (31, 30, 48),
    'Y': (228, 231, 132),
    'Z': (17, 26, 0),
    ' ': (233, 21, 8),
    ',': (231, 120, 93),
    '.': (205, 133, 214),
    '!': (251, 30, 124),
    '?': (173, 152, 244),
    ';': (1, 185, 151),
    ':': (113, 22, 11),
    '1': (111, 206, 86),
    '2': (222, 112, 236),
    '3': (222, 28, 144),
    '4': (132, 90, 219),
    '5': (253, 72, 239),
    '6': (128, 145, 244),
    '7': (47, 206, 110),
    '8': (177, 122, 148),
    '9': (58, 193, 52),
    '0': (122, 1, 20),
    '<': (225, 245, 132),
    '>': (155, 193, 40),
    'a': (213, 170, 121),
    'b': (152, 74, 21),
    'c': (132, 136, 11),
    'd': (143, 40, 215),
    'e': (239, 157, 112),
    'f': (16, 205, 215),
    'g': (151, 206, 84),
    'h': (162, 101, 110),
    'i': (11, 109, 27),
    'j': (30, 110, 233),
    'k': (101, 204, 19),
    'l': (86, 168, 89),
    'm': (189, 238, 136),
    'n': (103, 128, 102),
    'o': (247, 219, 183),
    'p': (23, 133, 193),
    'q': (209, 33, 163),
    'r': (248, 13, 45),
    's': (114, 192, 65),
    't': (201, 81, 223),
    'u': (4, 104, 120),
    'v': (212, 114, 0),
    'w': (255, 130, 221),
    'x': (166, 51, 154),
    'y': (126, 40, 229),
    'z': (153, 68, 164)
}

# Function to encrypt a message in an image
def encrypt_message(message,image_path):
    # Open the image
    img = Image.open(image_path)
    # Converts the image to RGB mode
    img = img.convert("RGB")
    # Gets the dimensions of the image
    width, height = img.size
    # Calculates the maximum message length
    max_length = (width * height)
    # Checks if the message is too long
    if len(message) > max_length:
        raise ValueError(f"The message is too long. Maximum length is {max_length}.")
    i = 0
    for y in range(height):
        for x in range(width):
            if i < len(message):
                # Encrypt the message by writing the color values to the pixels
                char = message[i]
                color = color_map[char]
                i += 1
            else:
                # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # color = tuple(img.getpixel((x, y)))
                color = (0, 0, 0)
            img.putpixel((x, y), color)
    # Saves the encrypted image
    img.save('encrypted.png')




# Function to decrypt a message from an image
def decrypt_message(image_path):
    img = Image.open(image_path)
    # Converts the image to RGB mode
    img = img.convert("RGB")
    # Gets the dimensions of the image
    width, height = img.size
    message = ''
    for y in range(height):
        for x in range(width):
            # Gets the color of the pixel
            color = tuple(img.getpixel((x, y)))
            # Finds the character that corresponds to the color
            char = None
            for key, value in color_map.items():
                # Finds the character that corresponds to the color
                if value == color:
                    char = key
                    break
            # If no character corresponds to the color, assume it's a filler pixel and ignore it
            if char is not None:
                message += char
    # Return the decrypted message
    return message

# Encrypt a message in an image
encrypt_message('download.png', 'this is a secret message')
# Decrypt the message from the encrypted image

print("Decrypting message...")
decrypted_message = decrypt_message('encrypted.png')
print("Decryption complete!")
print("Decrypted message: ", decrypted_message)
