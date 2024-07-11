from PIL import Image
import sys
import os
from pathlib import Path


def flip_image(image, flipped_image):
    img = Image.open(image)

    flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    flip_img.save(flipped_image)


def flip_images(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)
    # Check if image is a directory
    if os.path.isdir(input_path):
        images = [Path(input_path / image) for image in os.listdir(input_path)]
        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        for image in images:
            flip_image(image, output_path / image.name)
    else:
        flip_image(input_path, output_path)


def main(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(
        output_path
        if len(sys.argv) > 2
        else input_path.parent / (input_path.stem + "_flipped" + input_path.suffix)
    )

    flip_images(input_path, output_path)

    os.system("open " + str(output_path))


if __name__ == "__main__":
    # https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
    main(sys.argv[1], sys.argv[2])
