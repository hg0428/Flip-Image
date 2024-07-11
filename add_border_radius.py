from PIL import Image, ImageDraw


def add_transparent_border(
    image_path, output_path, size=1024, border_ratio=0.1, radius_ratio=0.2
):
    # Open the image
    image = Image.open(image_path).convert("RGBA")

    # Calculate border size and radius
    border_size = int(size * border_ratio)
    radius = int(size * radius_ratio)

    # Calculate new size with border
    original_size = image.size
    new_size = (original_size[0] + 2 * border_size, original_size[1] + 2 * border_size)

    # Create a new image with transparent background
    new_image = Image.new("RGBA", new_size, (0, 0, 0, 0))

    # Paste the original image onto the new image, centered
    new_image.paste(image, (border_size, border_size))

    # Create a mask with rounded corners
    mask = Image.new("L", new_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        [
            border_size,
            border_size,
            new_size[0] - border_size,
            new_size[1] - border_size,
        ],
        radius,
        fill=255,
    )

    # Apply the mask to the new image
    rounded_image = Image.new("RGBA", new_size)
    rounded_image.paste(new_image, (0, 0), mask=mask)

    # Save the resulting image
    rounded_image.save(output_path, format="PNG")


# Example usage
add_transparent_border("icons/icon.png", "icon_with_border_radius.png")
