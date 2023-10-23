from PIL import Image, ImageEnhance
import os

# ANSI escape codes for text color
RED_COLOR = "\033[91m"
GREEN_COLOR = "\033[92m"
BLUE_COLOR = "\033[94m"
RESET_COLOR = "\033[0m"

# Startup logo
STARTUP_LOGO = r"""
----------------------------------------------------------------
 █░█░█ ▄▀█ ▀█▀ █▀▀ █▀█ █▀▄▀█ ▄▀█ █▀█ █▄▀  █▄░█ █▀▀ █ █▄░█ █▀▀
 ▀▄▀▄▀ █▀█ ░█░ ██▄ █▀▄ █░▀░█ █▀█ █▀▄ █░█  █░▀█ █▄█ █ █░▀█ ██▄
---------------------------------------------------------------- 
"""

def calculate_watermark_position(image, watermark, watermark_position):
    image_width, image_height = image.size
    watermark_width, watermark_height = watermark.size

    if watermark_position == "BOTTOM_LEFT":
        return (0, image_height - watermark_height)
    elif watermark_position == "BOTTOM_RIGHT":
        return (image_width - watermark_width, image_height - watermark_height)
    elif watermark_position == "CENTER":
        return ((image_width - watermark_width) // 2, (image_height - watermark_height) // 2)
    elif watermark_position == "TOP_LEFT":
        return (0, 0)
    elif watermark_position == "TOP_RIGHT":
        return (image_width - watermark_width, 0)
    else:
        return None

def add_watermark(input_path, output_path, watermark_path, watermark_factor, watermark_opacity, watermark_position):
    watermark = Image.open(watermark_path)

    # Calculate new dimensions for the watermark image
    watermark_width = int(watermark.width * watermark_factor)
    watermark_height = int(watermark.height * watermark_factor)
    watermark = watermark.resize((watermark_width, watermark_height))

    watermark = watermark.convert("RGBA")
    watermark_with_opacity = Image.new("RGBA", watermark.size)
    for x in range(watermark.width):
        for y in range(watermark.height):
            r, g, b, a = watermark.getpixel((x, y))
            watermark_with_opacity.putpixel((x, y), (r, g, b, int(a * watermark_opacity)))

    for image_file in os.listdir(input_path):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(input_path, image_file)
            image = Image.open(image_path)

            if watermark_pos := calculate_watermark_position(
                image, watermark_with_opacity, watermark_position
            ):
                image.paste(watermark_with_opacity, watermark_pos, watermark_with_opacity)
                output_file = os.path.join(output_path, image_file)
                image.save(output_file)
                print(f"{BLUE_COLOR}Watermark added: {image_file}{RESET_COLOR}")
            else:
                print(f"Skipping {image_file}: Invalid watermark position")

    print(
        f"""{GREEN_COLOR}
---------------------------------------                                   
 █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ █▀▀ █▀▄
 █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ ██▄ █▄▀
---------------------------------------            
          """
    )

if __name__ == "__main__":
    input_folder = "data"
    output_folder = "watermarked_images"
    watermark_path = "static/watermark.png"
    watermark_factor = 0.10  # Increase size of the watermark (0.10 means 10%)
    watermark_opacity = 0.7  # Adjust the watermark opacity (0.7 means 70%)
    watermark_position = "BOTTOM_RIGHT"  # Change this to the desired position (TOP_RIGHT, TOP_LEFT, BOTTOM_RIGHT, BOTTOM_LEFT, CENTER)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(RED_COLOR + STARTUP_LOGO + RESET_COLOR)
    add_watermark(input_folder, output_folder, watermark_path, watermark_factor, watermark_opacity, watermark_position)

# ©️ Copyright Project Razer LLC 2023 All Rights Reserved.
# Credits: @sandarutharuneth
# License: CC0 1.0 Universal
