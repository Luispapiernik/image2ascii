from PIL import Image, ImageDraw

from image2ascii.schemas import Formats
from image2ascii.utils import get_gray_image, image_to_ascii

__all__ = ["convert_image"]


def convert_image(
    input_filename: str,
    output_filename: str,
    ascii_palette: str,
    format: str = Formats.TXT,
    ratio: float = 1,
) -> None:
    gray_image = get_gray_image(filename=input_filename)

    ascii_image = image_to_ascii(image=gray_image, ascii_color_palette=ascii_palette)

    if format == Formats.TXT:
        with open(f"{output_filename}.txt", "w") as file:
            for line in ascii_image:
                file.write("".join(line))
                file.write("\n")

    if format in ["png", "jpg", "jpeg"]:
        output_image = Image.new(
            mode="L", size=(gray_image.width, gray_image.height), color=255
        )
