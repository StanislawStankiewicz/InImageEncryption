from encoder import access_upper_right_square, binary_to_string


def decode_message(img, len_bits, size):
    decoded_bits = ''
    for pixel, x, y in access_upper_right_square(img, size=size):
        for i in range(3):
            value = pixel[i] & (2 ** len_bits - 1)
            decoded_bits += format(value, f'0{len_bits}b')
    decoded_message = binary_to_string(decoded_bits)
    try:
        decoded_message = decoded_message[:decoded_message.index('\x00')]
    except ValueError:
        pass
    return decoded_message
