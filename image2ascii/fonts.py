import subprocess
import sys
import warnings
from os.path import basename, splitext

# All the code in this file is taken from here
# https://github.com/pygame/pygame/blob/main/src_py/sysfont.py

OpenType_extensions = frozenset((".ttf", ".ttc", ".otf"))


def _simplename(name):
    """create simple version of the font name"""
    # return alphanumeric characters of a string (converted to lowercase)
    return "".join(c.lower() for c in name if c.isalnum())


def _addfont(name, bold, italic, font, fontdict):
    """insert a font and style into the font dictionary"""
    if name not in fontdict:
        fontdict[name] = {}
    fontdict[name][bold, italic] = font


def _parse_font_entry_unix(entry, fonts):
    """
    Parses an entry in the unix font data to add to the pygame font
    dictionary.
    :param entry: A entry from the unix font list.
    :param fonts: The pygame font dictionary to add the parsed font data to.
    """
    filename, family, style = entry.split(":", 2)
    if splitext(filename)[1].lower() in OpenType_extensions:
        bold = "Bold" in style
        italic = "Italic" in style
        oblique = "Oblique" in style
        for name in family.strip().split(","):
            if name:
                break
        else:
            name = splitext(basename(filename))[0]

        _addfont(_simplename(name), bold, italic or oblique, filename, fonts)


# read the fonts on unix
def get_system_fonts(path="fc-list"):
    """use the fc-list from fontconfig to get a list of fonts"""
    fonts = {}

    if sys.platform == "emscripten":
        return fonts

    try:
        proc = subprocess.run(
            [path, ":", "file", "family", "style"],
            stdout=subprocess.PIPE,  # capture stdout
            stderr=subprocess.PIPE,  # capture stderr
            check=True,  # so that errors raise python exception which is handled below
            timeout=1,  # so that we don't hang the program waiting
        )

    except FileNotFoundError:
        warnings.warn(
            f"'{path}' is missing, system fonts cannot be loaded on your platform"
        )

    except subprocess.TimeoutExpired:
        warnings.warn(
            f"Process running '{path}' timed-out! System fonts cannot be loaded on "
            "your platform"
        )

    except subprocess.CalledProcessError as e:
        warnings.warn(
            f"'{path}' failed with error code {e.returncode}! System fonts cannot be "
            f"loaded on your platform. Error log is:\n{e.stderr}"
        )

    else:
        for entry in proc.stdout.decode("ascii", "ignore").splitlines():
            try:
                _parse_font_entry_unix(entry, fonts)
            except ValueError:
                # try the next one.
                pass

    return fonts
