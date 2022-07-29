from typing import List

from PIL import Image

AsciiImage = List[List[str]]


def get_gray_image(filename: str) -> Image.Image:
    img = Image.open(filename)
    gray = img.convert('L')
    img.close()

    return gray


def image_to_ascii(image: Image.Image, ascii_color_palette: str) -> AsciiImage:
    pixels = image.getdata()

    groups_number = 256 / len(ascii_color_palette)
    char_data = [
        ascii_color_palette[int(pixel / groups_number)]
        for pixel in pixels
    ]

    ascii_image = [
        char_data[index: index + image.width]
        for index in range(0, len(char_data), image.width)
    ]

    return ascii_image
