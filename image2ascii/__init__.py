from PIL import Image, ImageDraw

from image2ascii.utils import get_gray_image, image_to_ascii

__all__ = ["convert_image"]

# Taken from here http://paulbourke.net/dataformats/asciiart/
LONG_GRAY_SCALE_1 = (
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
)
LONG_GRAY_SCALE_2 = (
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."
)
SHORT_GRAY_SCALE_1 = "@%#*+=-:. "
SHORT_GRAY_SCALE_2 = "@%#*+=-:."
OPTION_1 = "@JD%*P+Y$,."
OPTION_2 = "@JD%*P+Y$,. "


def convert_image(
    input_filename: str, output_filename: str, format: str = "txt"
) -> None:
    gray_image = get_gray_image(filename=input_filename)

    ascii_image = image_to_ascii(
        image=gray_image, ascii_color_palette=SHORT_GRAY_SCALE_2
    )

    if format == "txt":
        with open(f"{output_filename}.txt", "w") as file:
            for line in ascii_image:
                file.write("".join(line))
                file.write("\n")

    if format in ["png", "jpg", "jpeg"]:
        output_image = Image.new(
            mode="L", size=(gray_image.width, gray_image.height), color=255
        )
