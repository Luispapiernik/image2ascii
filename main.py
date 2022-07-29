from argparse import ArgumentParser

from image2ascii import convert_image


DESCRIPTION = '''This program converts an image to
ASCII and saves it in png and txt files'''

FORMAT_HELP = '''PNG tells the program that the output is an
image, TXT indicates the output is in plain text and
and BOTH indicates both formats'''

INVERT_HELP = '''invert output image. Use if your display has
a dark background'''


def execute(args):
    convert_image(input_filename=args.input, output_filename=args.output)


def main() -> None:
    parser = ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        '-i', '--input', type=str, metavar='INPUT',
        help='name of the input image'
    )
    parser.add_argument(
        '-o', '--output', default='ascii', type=str,
        help='names of the output file without format'
    )
    parser.add_argument(
        '--format', default='PNG', metavar='PNG/TXT/BOTH',
        choices=['PNG', 'TXT', 'BOTH'], help=FORMAT_HELP,
    )
    parser.add_argument(
        '-f', '--font', default='', type=str,
        help='font to be used for the conversion'
    )
    parser.add_argument(
        '--invert', action='store_true', help=INVERT_HELP
    )

    args = parser.parse_args()
    execute(args)


if __name__ == "__main__":
    main()
