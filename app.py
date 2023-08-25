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

def add_watermark(input_path, output_path, watermark_path, watermark_width_factor, watermark_height_factor, watermark_opacity, watermark_position):
    watermark = Image.open(watermark_path)
    
    # Calculate new dimensions for the watermark image
    new_width = int(watermark.width * watermark_width_factor)
    new_height = int(watermark.height * watermark_height_factor)
    watermark = watermark.resize((new_width, new_height))
    
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
            if watermark_position == "TOP_RIGHT":
                watermark_position = (image.width - watermark_with_opacity.width, 0)
            elif watermark_position == "BOTTOM_RIGHT":
                watermark_position = (image.width - watermark_with_opacity.width, image.height - watermark_with_opacity.height)
            elif watermark_position == "TOP_LEFT":
                watermark_position = (0, 0)
            elif watermark_position == "BOTTOM_LEFT":
                watermark_position = (0, image.height - watermark_with_opacity.height)
            elif watermark_position == "CENTER":
                watermark_position = ((image.width - watermark_with_opacity.width) // 2, (image.height - watermark_with_opacity.height) // 2)
            image.paste(watermark_with_opacity, watermark_position, watermark_with_opacity)
            output_file = os.path.join(output_path, image_file)
            image.save(output_file)
            print(BLUE_COLOR + f"Watermark added: {image_file}" + RESET_COLOR)

    print(GREEN_COLOR + f"""
---------------------------------------                                   
 █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ █▀▀ █▀▄
 █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ ██▄ █▄▀
---------------------------------------            
          """ )

if __name__ == "__main__":
    input_folder = "data"
    output_folder = "watermarked_images"
    watermark_path = "static/watermark.png"
    watermark_width_factor = 0.8  # Adjust the watermark width (0.8 means 80%)
    watermark_height_factor = 0.8  # Adjust the watermark height (0.8 means 80%)
    watermark_opacity = 0.7  # Adjust the watermark opacity (0.7 means 70%)
    watermark_position = "TOP_LEFT"  # Change this to the desired position
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(RED_COLOR + STARTUP_LOGO + RESET_COLOR)
    add_watermark(input_folder, output_folder, watermark_path, watermark_width_factor, watermark_height_factor, watermark_opacity, watermark_position)
