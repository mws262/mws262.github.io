import sys
from PIL import Image

def resize_to_200x200(input_path, output_path):
    im = Image.open(input_path)
    width, height = im.size

    if width < height:
        new_width = 200
        new_height = int(height * 200 / width)
        im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
        top = (new_height - 200) // 2
        im = im.crop((0, top, 200, top + 200))
    else:
        new_height = 200
        new_width = int(width * 200 / height)
        im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
        left = (new_width - 200) // 2
        im = im.crop((left, 0, left + 200, 200))

    im.save(output_path, format='WEBP')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python resize_webp.py input.webp output.webp")
        sys.exit(1)
    resize_to_200x200(sys.argv[1], sys.argv[2])
