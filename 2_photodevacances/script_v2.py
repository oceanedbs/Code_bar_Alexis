import re
from functools import reduce

def calculate_key(filename):
    # Step 1: Extract punctuation from key.txt
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Use regex to find all non-word characters excluding whitespace
    punctuation_marks = re.findall(r'[^\w\s]', text)
    print(punctuation_marks)
    
    # Step 2: Calculate the ASCII product
    ascii_values = [ord(char) for char in punctuation_marks]
    product = reduce(lambda x, y: x * y, ascii_values, 1)
    
    # Step 3: Multiply by 1996, take modulo 1705 and then modulo 256
    key = (product * 1996) % 1705 % 256
    return key

def xor_image(input_image, output_image, key):
    # Step 4: XOR each byte in the image with the key
    with open(input_image, "rb") as img_file:
        image_data = img_file.read()
    
    xored_data = bytes([byte ^ key for byte in image_data])
    
    # Write the decoded image to a new file
    with open(output_image, "wb") as out_file:
        out_file.write(xored_data)

# Usage
key = calculate_key("2_photodevacances/key.txt")
print(f"The computed XOR key is: {key}")

# Apply XOR to decode the image
xor_image('2_photodevacances/codeimage.jpg', '2_photodevacances/new_image.jpg', key)
