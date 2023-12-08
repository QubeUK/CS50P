import sys
from PIL import Image,ImageOps

def main():
    inputf, outputf = read_argv()
    convert(inputf,outputf)

def convert(inputf, outputf):
    image_1 = Image.open(inputf)
    shirt = Image.open("shirt.png")
    size = shirt.size
    image_2 = ImageOps.fit(image_1, size)
    image_2.paste(shirt, shirt)
    image_2.save(outputf)
    return

def read_argv():
    argv_in = 3                     #Amount of expected command line arguments (program + args)
    exts = ".png",".jpg",".jpeg"    #Tuple with extenstion to check for in arguments
    while True:
        try:
            if len(sys.argv) == argv_in and sys.argv[1].endswith((exts)) and sys.argv[2].endswith((exts)):
                ext1 = sys.argv[1].rpartition('.')[-1]
                ext2 = sys.argv[2].rpartition('.')[-1]
                if ext1 == ext2:
                    try:
                        with open(sys.argv[1]) as file:
                            return sys.argv[1], sys.argv[2]
                    except FileNotFoundError:
                        sys.exit(f"Could not read {sys.argv[1]}")
                else:
                    sys.exit("Input and output have different extensions")
            elif len(sys.argv) == argv_in and not sys.argv[1].endswith((exts)):
                    sys.exit("Not an image file")
            elif len(sys.argv) == argv_in and not sys.argv[2].endswith((exts)):
                    sys.exit("Invalid output")
            elif len(sys.argv) < argv_in:
                    sys.exit("Too few command-line arguments")
            elif len(sys.argv) > argv_in:
                    sys.exit("Too many command-line arguments")
            else:
                continue
        finally:
                pass


if __name__ == "__main__":
    main()
