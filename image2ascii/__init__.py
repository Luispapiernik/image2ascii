import numpy as np
from PIL import Image

from image2ascii.schemas import Visualizers
from image2ascii.utils import get_gray_image, image_to_ascii

__all__ = ["convert_image"]


def convert_image(
    input_filename: str,
    output_filename: str,
    ascii_palette: str,
    format: str = Visualizers.TXT,
    ratio: float = 1,
) -> None:
    gray_image = get_gray_image(filename=input_filename)

    ascii_image = image_to_ascii(
        image_array=np.array(gray_image), ascii_palette=ascii_palette, ratio=ratio
    )

    if format == Visualizers.TXT:
        with open(f"{output_filename}.txt", "w") as file:
            for line in ascii_image:
                file.write("".join(line))
                file.write("\n")

    if format in ["png", "jpg", "jpeg"]:
        output_image = Image.new(
            mode="L", size=(gray_image.width, gray_image.height), color=255
        )
