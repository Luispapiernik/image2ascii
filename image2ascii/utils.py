import math
from typing import List, Tuple

import numpy as np
from PIL import Image

AsciiImage = List[List[str]]


def get_gray_image(filename: str) -> Image.Image:
    img = Image.open(filename)
    gray = img.convert("L")
    img.close()

    return gray


def group_index(size: int, group_number: int) -> Tuple[int, int]:
    remainder = size % group_number

    group_sizes = [size // group_number] * group_number
    index = math.ceil(remainder / 2) - 1
    while remainder > 0:
        group_sizes[index] += 1
        index = (index - 1) % group_number
        remainder -= 1

    last_index = 0
    for group_size in group_sizes:
        yield last_index, group_size
        last_index += group_size


def convolve(array, target_width, target_height, function):
    convolved_matrix = []
    for index, h_size in group_index(array.shape[0], target_height):
        convolved_matrix.append([])
        for jndex, w_size in group_index(array.shape[1], target_width):
            convolved_matrix[-1].append(
                function(array[index : index + h_size, jndex : jndex + w_size])
            )

    return np.array(convolved_matrix)


def image_to_ascii(
    image_array: np.array,
    ascii_palette: str,
    ratio: float = 0.315,
    aggregation_funcion_name="mean",
) -> AsciiImage:
    get_color = {"mean": np.mean, "max": np.max, "min": np.min}[
        aggregation_funcion_name
    ]

    spectrum_length = len(ascii_palette) - 1
    ascii_image = convolve(
        image_array,
        image_array.shape[1],
        int(ratio * image_array.shape[0]),
        function=lambda x: ascii_palette[int(spectrum_length * get_color(x) / 255)],
    )

    return ascii_image
