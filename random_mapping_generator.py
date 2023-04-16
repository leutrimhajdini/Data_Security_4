import random

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?;:<>"

char_to_rgb = {}

for char in alphabet:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    char_to_rgb[char] = (r, g, b)

print(char_to_rgb)
