## Pixel Art Generator Tutorial

This tutorial will guide you through generating colorful pixel art images procedurally using Python lists to represent the pixel data and the Pillow library for image manipulation. We'll focus on creating a simple, repeating pattern to demonstrate the core concepts.

# Import necessary library
# Pillow (PIL fork) is a powerful image processing library for Python.
# If you don't have it installed, run: pip install Pillow
from PIL import Image

# --- 1. Defining the Pixel Grid ---
# We'll represent our pixel art as a 2D grid (a list of lists).
# Each inner list represents a row of pixels, and each element
# in the inner list represents the color of a single pixel.

# Define the dimensions of our pixel art grid (width, height).
# These are kept small for simplicity in this tutorial.
GRID_WIDTH = 32
GRID_HEIGHT = 32

# Define a color palette.
# Colors are represented as RGB tuples (Red, Green, Blue), where
# each value ranges from 0 to 255.
# We'll create a simple palette with a few distinct colors.
COLOR_PALETTE = [
    (50, 50, 50),     # Dark Gray
    (200, 200, 200),  # Light Gray
    (0, 100, 200),    # Blue
    (255, 150, 0)     # Orange
]

# --- 2. Generating the Pixel Data (The "Art" Part) ---
# This is where we'll define the logic for our pixel art.
# For this tutorial, we'll create a simple checkerboard-like pattern
# that alternates colors based on the pixel's position.

def generate_pixel_data(width: int, height: int, palette: list[tuple[int, int, int]]) -> list[list[tuple[int, int, int]]]:
    """
    Generates a 2D list representing pixel data for an image.

    Args:
        width: The desired width of the image in pixels.
        height: The desired height of the image in pixels.
        palette: A list of RGB color tuples to choose from.

    Returns:
        A list of lists, where each inner list is a row of pixels,
        and each pixel is an RGB color tuple.
    """
    pixel_grid = []  # Initialize an empty list to hold all rows

    # Iterate through each row of the grid
    for y in range(height):
        row = []  # Initialize an empty list for the current row
        # Iterate through each column (pixel) in the current row
        for x in range(width):
            # --- The Pattern Logic ---
            # We'll use a simple condition to decide which color to use.
            # The modulo operator (%) is very useful here for creating repeating patterns.
            # (x % 2) checks if the x-coordinate is even or odd.
            # (y % 2) checks if the y-coordinate is even or odd.
            # Combining these allows for a checkerboard effect.

            if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
                # If both x and y are even, or both are odd, use the first color (index 0)
                color_index = 0
            else:
                # Otherwise (one is even, one is odd), use the second color (index 1)
                color_index = 1

            # Alternatively, we could use the palette index directly for more complex patterns.
            # For example, to cycle through colors:
            # color_index = (x + y) % len(palette)

            # Get the color from the palette using the calculated index
            selected_color = palette[color_index]

            # Add the selected color to the current row
            row.append(selected_color)

        # Add the completed row to the pixel grid
        pixel_grid.append(row)

    return pixel_grid

# --- 3. Creating the Image from Pixel Data ---
# Now that we have our pixel data, we need to turn it into an actual image file.

def create_image_from_pixels(pixel_data: list[list[tuple[int, int, int]]], output_filename: str):
    """
    Creates an image file from a 2D list of pixel data.

    Args:
        pixel_data: A list of lists representing the pixel grid.
        output_filename: The name of the image file to save (e.g., "my_art.png").
    """
    # Get the dimensions from the pixel_data
    height = len(pixel_data)
    if height == 0:
        print("Error: Pixel data is empty.")
        return
    width = len(pixel_data[0])
    if width == 0:
        print("Error: Pixel data rows are empty.")
        return

    # Create a new RGB image with the specified dimensions.
    # Image.new('RGB', (width, height)) creates a blank image.
    img = Image.new('RGB', (width, height))

    # Iterate through each row and each pixel to set its color in the image.
    for y in range(height):
        for x in range(width):
            # Get the color for the current pixel from our pixel_data
            color = pixel_data[y][x]
            # Set the pixel at coordinates (x, y) to the specified color.
            img.putpixel((x, y), color)

    # Save the image to a file.
    try:
        img.save(output_filename)
        print(f"Image saved successfully as {output_filename}")
    except IOError:
        print(f"Error: Could not save image to {output_filename}")

# --- Example Usage ---
if __name__ == "__main__":
    # This block only runs when the script is executed directly (not imported as a module).

    print("Generating pixel art...")

    # 1. Generate the pixel data using our function.
    # We pass the desired grid dimensions and our color palette.
    generated_data = generate_pixel_data(GRID_WIDTH, GRID_HEIGHT, COLOR_PALETTE)

    # 2. Create the image file from the generated pixel data.
    # We specify a filename for the output image.
    create_image_from_pixels(generated_data, "my_pixel_art.png")

    print("Done!")