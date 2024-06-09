from math import ceil, sqrt


def encode_message(img, message, len_bits, *, size='auto'):
    if size == 'auto':
        message_bits = len(message) * 7 + 7
        size = ceil(sqrt(int(message_bits / (3 * len_bits)) + 1))
        print(f'Encoding image with size={size}')

    binary = string_to_binary(message)
    img_data = img.load()
    bits = (int(b) for b in binary)
    bit_count = 0
    count = 0
    stop = False

    for pixel, x, y in access_upper_right_square(img, size=size):
        new_pixel = [pixel[i] for i in range(4)]

        for i in range(3):
            value = get_n_bits(bits, len_bits)
            new_pixel[i] = change_last_bits(pixel[i], value, len_bits)
            bit_count += len_bits
            if bit_count >= 7:
                count = 0
                bit_count = 0
            if value == 0:
                count += len_bits
            if count >= 7:
                stop = True
                break
        img_data[x, y] = tuple(new_pixel)
        if stop:
            break


def change_last_bits(value, bits, len_bits):
    mask = 255 - (2 ** len_bits - 1)
    return (value & mask) | bits


def access_upper_right_square(img, *, size):
    img_data = img.load()
    for x in range(img.width - size, img.width):
        for y in range(size):
            yield img_data[x, y], x, y


def next_or_0(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return 0


def get_n_bits(iterator, len_bits):
    bits = 0
    for i in range(len_bits):
        bits = (bits << 1) | next_or_0(iterator)
    return bits


def string_to_binary(test_str):
    res = ''.join(format(ord(i), '07b') for i in test_str)
    return res


if __name__ == "__main__":
    import sys

    if len(sys.argv) <= 2:
        print("Specify image name")

    elif sys.argv[1] == "--h" or sys.argv[1] == "-help":
        print("Image encoder. Example usage:")
        print(" python encoder.py example.png encoded.png Text to be encoded")

    else:
        from PIL import Image

        image_name = sys.argv[1]
        encoded_name = sys.argv[2]
        message = ' '.join(sys.argv[3:])

        img = Image.open(image_name)

        len_bits = 6
        encode_message(img, message, len_bits)
        img.save(encoded_name)