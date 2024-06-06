from PIL import Image
from encoder import encode_message
from decoder import decode_message


img = Image.open('example.png')

message = 'Wybrane problemy ochrony informacji'
len_bits = 6
encode_message(img, message, len_bits)
img.save('encoded.png')

img = Image.open('encoded.png')
decoded_message = decode_message(img, 6, size=4)
print(decoded_message)

