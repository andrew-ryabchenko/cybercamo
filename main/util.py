from io import BytesIO
from bitstring import BitArray
from PIL import Image
from django.http import FileResponse

def obfuscate_via_lsb(data_file, input_file) -> BytesIO | None:

    data = data_file.read()
    data = BitArray(uint=len(data) * 8, length=32).bin + BitArray(bytes=data).bin

    i = 0

    with Image.open(input_file) as img:
        width, height = img.size
        if len(data) > width * height * 3:
            print(("Data is too large to be embedded in the image."
                   f"Data contains {int(len(data) / 8)} bytes,"
                   f"maximum is {int(width * height * 3 / 8)}"))
            return None
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    if i < len(data):
                        pixel[n] = pixel[n] & ~1 | int(data[i])
                        i += 1
                img.putpixel((x, y), tuple(pixel))
                if i >= len(data):
                    break
            if i >= len(data):
                break

        temp_bytes = BytesIO()

        img.save(temp_bytes, format="png")

        temp_bytes.seek(0)

        return temp_bytes

def deobfuscate_via_lsb(input_file) -> BytesIO:
    img = Image.open(input_file)
    payload_length = int("".join([str(x) for x in decode_img_nbits(img, 32)]), 2)
    data = decode_img_nbits(img, payload_length + 32)[32:]
    data = BitArray(bin="".join([str(x) for x in data])).bytes
    return BytesIO(data)

def decode_img_nbits(img, nbits):
    data = []
    i = 0
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))
            for n in range(0, 3):
                if i < nbits:
                    data.append(pixel[n] & 1)
                    i += 1
            if i >= nbits:
                break
        if i >= nbits:
            break
    return data

def make_attachment_response(output_file, filename):
    response = FileResponse(output_file, as_attachment=True, filename=filename)
    response["Content-Type"] = "application/octet-stream"
    return response
