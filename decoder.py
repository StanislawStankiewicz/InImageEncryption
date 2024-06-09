from encoder import access_upper_right_square


def binary_to_string(binary):
    res = bytearray(int(binary[i: i + 7], 2) for i in range(0, len(binary), 7)).decode()
    return res


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


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Specify image name")

    elif sys.argv[1] == "--h" or sys.argv[1] == "-help":
        print("Image decoder. Example usage:")
        print(" python decoder.py encoded.png")

    else:
        from PIL import Image

        image_name = sys.argv[1]
        img = Image.open(image_name)
        decoded_message = decode_message(img, 6, size=4)
        print(decoded_message)