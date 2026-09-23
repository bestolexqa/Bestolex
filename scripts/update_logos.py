import os
from PIL import Image

def process_logos():
    src_path = 'scripts/Bestolex-Logo.png'
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Source file not found: {src_path}")
    
    img = Image.open(src_path).convert('RGBA')
    width, height = img.size
    print(f"Original image size: {width}x{height}")
    
    # 1. Save original transparent logo to public/logo.png
    img.save('public/logo.png', 'PNG')
    print("Saved public/logo.png successfully.")
    
    # 2. Generate dark mode logo: convert black/dark text to white (255, 255, 255)
    # Keeping golden (233, 158, 5) and gray (111, 112, 112) unchanged
    pixels = img.load()
    dark_img = Image.new('RGBA', (width, height))
    dark_pixels = dark_img.load()
    
    dark_pixels_count = 0
    gold_pixels_count = 0
    gray_pixels_count = 0
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                dark_pixels[x, y] = (255, 255, 255, 0)
            elif r <= 45 and g <= 45 and b <= 45:
                # Black/dark text pixel -> convert to pure white with same alpha
                dark_pixels[x, y] = (255, 255, 255, a)
                dark_pixels_count += 1
            else:
                # Gold, gray or other colored pixels -> keep original
                dark_pixels[x, y] = (r, g, b, a)
                if r > 180 and g > 120 and b < 50:
                    gold_pixels_count += 1
                elif abs(r - g) <= 5 and abs(g - b) <= 5 and r > 80:
                    gray_pixels_count += 1
                    
    dark_img.save('public/logo-dark-transparent.png', 'PNG')
    print(f"Saved public/logo-dark-transparent.png successfully.")
    print(f"Processed: {dark_pixels_count} dark pixels inverted to white, {gold_pixels_count} gold pixels kept, {gray_pixels_count} gray pixels kept.")

if __name__ == '__main__':
    process_logos()
