from enum import Enum, IntEnum


class Palettes(Enum):
    # Taken from here http://paulbourke.net/dataformats/asciiart/
    LONG_WITH_WHITE = (
        " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    )
    LONG_WITHOUT_WHITE = (
        ".'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    )
    SHORT_WITH_WHITE = " .:-=+*#%@"
    SHORT_WITHOUT_WHITE = ".:-=+*#%@"
    SHORT_DENSE_WITH_WHITE = " .,$Y+P*%DJ@"
    SHORT_DENSE_WITHOUT_WHITE = ".,$Y+P*%DJ@"


class Visualizers(IntEnum):
    TXT = 1
    CURSES = 2
    PNG = 4
    PYGAME = 8
