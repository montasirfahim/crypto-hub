import os
from PIL import Image

def message_to_bin(message):
    if isinstance(message, str):
        return ''.join([format(ord(i), "08b") for i in message])
    elif isinstance(message, bytes) or isinstance(message, bytearray):
        return ''.join([format(i, "08b") for i in message])
    elif isinstance(message, int):
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")

def encode_image(image_path, secret_message, output_path):
    img = Image.open(image_path)
    # Convert image to RGB if it's not
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = img.load()
    width, height = img.size
    
    # Adding a delimiter to indicate the end of the message
    secret_message += "#####"
    binary_message = message_to_bin(secret_message)
    data_len = len(binary_message)
    
    if data_len > width * height * 3:
        raise ValueError("Message too large for this image")
    
    data_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            if data_index < data_len:
                r = (r & ~1) | int(binary_message[data_index])
                data_index += 1
            if data_index < data_len:
                g = (g & ~1) | int(binary_message[data_index])
                data_index += 1
            if data_index < data_len:
                b = (b & ~1) | int(binary_message[data_index])
                data_index += 1
            
            pixels[x, y] = (r, g, b)
            
            if data_index >= data_len:
                # Always save as PNG to avoid lossy compression
                output_path = os.path.splitext(output_path)[0] + ".png"
                img.save(output_path, "PNG")
                return output_path
    return False

def decode_image(image_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = img.load()
    width, height = img.size
    
    binary_data = ""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
            
    # Convert binary to string
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_message = ""
    for byte in all_bytes:
        decoded_message += chr(int(byte, 2))
        if decoded_message.endswith("#####"):
            return decoded_message[:-5]
            
    return "No message found or delimiter missing"
