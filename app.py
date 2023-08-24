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

def add_watermark(input_path, output_path, watermark_path):
    watermark = Image.open(watermark_path)
    
    # Calculate new dimensions for the watermark image (0.8X)
    new_width = int(watermark.width * 0.8)
    new_height = int(watermark.height * 0.8)
    watermark = watermark.resize((new_width, new_height))
    
    watermark = watermark.convert("RGBA")
    watermark_with_opacity = Image.new("RGBA", watermark.size)
    for x in range(watermark.width):
        for y in range(watermark.height):
            r, g, b, a = watermark.getpixel((x, y))
            watermark_with_opacity.putpixel((x, y), (r, g, b, int(a * 0.7)))

    for image_file in os.listdir(input_path):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(input_path, image_file)
            image = Image.open(image_path)
            watermark_position = (image.width - watermark_with_opacity.width, image.height - watermark_with_opacity.height)
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

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(RED_COLOR + STARTUP_LOGO + RESET_COLOR)
    add_watermark(input_folder, output_folder, watermark_path)
