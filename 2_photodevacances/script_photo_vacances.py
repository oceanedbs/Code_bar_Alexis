import string
from PIL import Image
import io

def get_punctuation(input_string):
    return ''.join([char for char in input_string if char in string.punctuation])

def get_ascii_code(character):
    return ord(character)

#open file key.txt as a string
with open("2_photodevacances/key.txt", 'r') as file:
    file_content =  file.read()

def read_image_as_byte_table(file_path):
    with open(file_path, 'rb') as file:
        byte_table = list(file.read())
    return byte_table

# Save the new_image byte string as a JPEG file
def save_as_jpeg(byte_string, output_path):
    with open(output_path, 'wb') as file:
        file.write(byte_string)
        
def xor_bytes(data: bytes, key: int) -> bytes:
    res = []
    for d in data:
        res.append(d^key)
    return res

# Get punctuation
puctuation = get_punctuation(file_content)
print(puctuation)

#Compute key
res=1
for p in puctuation:
    res *= get_ascii_code(p)
    print(get_ascii_code(p))
final_res = (res  * 1996) % 1705 % 256
print(final_res)

file_path = '2_photodevacances/codeimage.jpg'
byte_table = read_image_as_byte_table(file_path)
print(byte_table[:10])

# Apply XOR on byte_table
new_image = xor_bytes(byte_table, final_res)
print(new_image[:10])


output_path = '2_photodevacances/new_image.jpg'
save_as_jpeg(bytes(new_image), output_path)


image = Image.open(io.BytesIO(bytes(new_image)))
image.show()