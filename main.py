from argparse import ArgumentParser

from image2ascii import convert_image
from image2ascii.fonts import get_system_fonts
from image2ascii.schemas import Formats, Palettes

DESCRIPTION = """This program converts an image to
ASCII and saves it in png and txt files"""

FORMAT_HELP = """PNG tells the program that the output is an
image, TXT indicates the output is in plain text and
and BOTH indicates both formats"""

INVERT_HELP = """invert output image. Use if your display has
a dark background"""


def execute(args):
    convert_image(
        input_filename=args.input,
        output_filename=args.output,
        ascii_palette=args.custom_palette,
        format=args.format,
        ratio=args.ratio,
    )


def main() -> None:
    parser = ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "-i", "--input", type=str, metavar="INPUT", help="name of the input image"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="ascii",
        type=str,
        help="names of the output file without format",
    )
    formats = {format.name: format for format in Formats}
    parser.add_argument(
        "--format",
        default="TXT",
        choices=formats.keys(),
        type=str,
        help=FORMAT_HELP,
    )

    ascii_palettes = {palette.name: palette.value for palette in Palettes}
    parser.add_argument(
        "-ap",
        "--ascii-palette",
        default="SHORT_WITH_WHITE",
        type=str,
        choices=ascii_palettes.keys(),
    )
    parser.add_argument("-cp", "--custom-palette", type=str, default="")
    parser.add_argument("--invert-palette", action="store_true", help=INVERT_HELP)
    parser.add_argument("-r", "--ratio", default=1, type=float)

    system_fonts = get_system_fonts()
    parser.add_argument(
        "-f",
        "--font-name",
        default="",
        type=str,
        help="font to be used for the conversion",
        choices=system_fonts.keys(),
    )
    parser.add_argument("--font-path", default="", type=str)

    args = parser.parse_args()
    args.format = formats[args.format]

    if not args.font_path and args.font_name:
        args.font_path = system_fonts[args.font_name].get(
            (False, False), list(system_fonts[args.font_name].values())[0]
        )
    if not args.custom_palette:
        args.custom_palette = ascii_palettes[args.ascii_palette]

    if args.invert_palette:
        args.custom_palette = args.custom_palette[::-1]

    execute(args)


if __name__ == "__main__":
    main()
