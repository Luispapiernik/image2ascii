from enum import Enum


class Palettes(Enum):
    # Taken from here http://paulbourke.net/dataformats/asciiart/
    LONG_WITH_WHITE = (
        "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    )
    LONG_WITHOUT_WHITE = (
        "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."
    )
    SHORT_WITH_WHITE = "@%#*+=-:. "
    SHORT_WITHOUT_WHITE = "@%#*+=-:."
    SHORT_DENSE_WITH_WHITE = "@JD%*P+Y$,. "
    SHORT_DENSE_WITHOUT_WHITE = "@JD%*P+Y$,."


class Formats(Enum):
    TXT = "TXT"
    PNG = "PNG"
    BOTH = "BOTH"
