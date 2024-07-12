# In Image Text Encryption

> Steganography is the practice of representing information within another message or physical object, in such a manner that the presence of the information is not evident to human inspection. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video.<sup>[1](https://en.wikipedia.org/wiki/Steganography)</sup>

**How it works:**
1. **Text to Binary**: The script converts the input text into binary format.
2. **Encoding**: It embeds the binary data into the least significant bits of the pixel values in the image.
3. **Decoding**: To retrieve the original text, the script extracts the binary data from the image and converts it back into text. For this to work, the number of bits and the size that was used must be supplied.

**Usage:**
1. Clone the repository or download the script.
2. Provide an input text and an image for encoding.
3. Run the script to generate the encoded image.
4. To decode, use the provided encoded image and run the script again.

**Dependencies:**
- Python 3.x
- Pillow (Python Imaging Library)

# Example

For clear view I will use a white 10x10 image and 6 least significant bits.

<p align="center">
  <img src="https://github.com/StanislawStankiewicz/InImageEncryption/assets/60826828/a8c73983-0de8-42b2-8b5f-607ee004de7b" alt="white" width="300" height="300">
</p>

Now I will load it and encode the string `"Wybrane problemy ochrony informacji"` in it.
```python
img = Image.open('example.png')

message = 'Wybrane problemy ochrony informacji'
len_bits = 6
encode_message(img, message, len_bits)
img.save('encoded.png')
```
And this is the result:

<p align="center">
  <img src="https://github.com/StanislawStankiewicz/InImageEncryption/assets/60826828/9b866908-eb17-4ce3-9869-35a6b235a15c" alt="encoded" width="300" height="300">
</p>

Now I can load the encoded image and decode it providing neccessary information.
```python
img = Image.open('encoded.png')
decoded_message = decode_message(img, 6, size=4)
print(decoded_message)
```
Output: `Wybrane problemy ochrony informacji`

---

**References:**
- [Wikipedia - Steganography](https://en.wikipedia.org/wiki/Steganography)
