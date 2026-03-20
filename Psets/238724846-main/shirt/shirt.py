import sys
import os
from PIL import Image, ImageOps



def main():
    extensions = (".jpg", ".jpeg", ".png",)
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments ")

    bfr_img = os.path.splitext(sys.argv[1])[1].lower()
    aft_img = os.path.splitext(sys.argv[2])[1].lower()

    if not ((bfr_img in extensions) and (aft_img in  extensions)):
        sys.exit("Not a correct file type!")

    elif not bfr_img == aft_img:
        sys.exit("Input and output have different extensions")
    try:
        with open(f"{sys.argv[1]}") as f:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")

    overlay()



def overlay():
    base = Image.open(sys.argv[1])

    overlay = Image.open("shirt.png")

    base = ImageOps.fit(base, overlay.size)
    base.paste(overlay, None, overlay)

    base.save(sys.argv[2])





if __name__ == "__main__":
    main()
