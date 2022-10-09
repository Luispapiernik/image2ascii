from argparse import ArgumentParser

from image2ascii import convert_image
from image2ascii.fonts import get_system_fonts
from image2ascii.schemas import Palettes, Visualizers

DESCRIPTION = """this program converts an image to
ASCII and saves it in png and txt files"""

VISUALIZER_HELP = """indicates where the output of the
image will go: plain text file (TXT), terminal with curses (CURSES),
png image (PNG), pygame (PYGAME) or a combination of all of them"""

INVERT_HELP = """invert output image. Use if your display has
a dark background"""

ASCII_PALETTES = {palette.name: palette.value for palette in Palettes}
SYSTEM_FONTS = get_system_fonts()


def execute(args):
    if not args.font_path and args.font_name:
        args.font_path = SYSTEM_FONTS[args.font_name].get(
            (False, False), list(SYSTEM_FONTS[args.font_name].values())[0]
        )
    if not args.custom_palette:
        args.custom_palette = ASCII_PALETTES[args.ascii_palette]

    if args.invert_palette:
        args.custom_palette = args.custom_palette[::-1]

    if args.show_system_fonts:
        print(SYSTEM_FONTS.keys())
        exit(0)

    convert_image(
        input_filename=args.input,
        output_filename=args.output,
        ascii_palette=args.custom_palette,
        format=args.visualizer,
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
    visualizers = {visualizer.name: visualizer.value for visualizer in Visualizers}
    parser.add_argument(
        "--visualizer",
        default=1,
        type=lambda x: visualizers[x] if not x.isdigit() else int(x),
        help=VISUALIZER_HELP,
    )

    parser.add_argument(
        "-ap",
        "--ascii-palette",
        default="SHORT_WITH_WHITE",
        type=str,
        choices=ASCII_PALETTES.keys(),
    )
    parser.add_argument("-cp", "--custom-palette", type=str, default="")
    parser.add_argument("--invert-palette", action="store_true", help=INVERT_HELP)
    parser.add_argument("-r", "--ratio", default=0.315, type=float)

    parser.add_argument(
        "-sf",
        "--show-system-fonts",
        action="store_true",
        help="show the available system fonts",
    )
    parser.add_argument(
        "-f",
        "--font-name",
        default="",
        type=str,
        help="font to be used for the conversion. The best option is monospaced fonts",
    )
    parser.add_argument("--font-path", default="", type=str)

    args = parser.parse_args()
    execute(args)


if __name__ == "__main__":
    main()
