import math
from PIL import Image
from typing import List, Tuple

Pixels = List[Tuple[int, int, int]]

def load_pixels(image: Image) -> Pixels:
    width, height = image.size
    pixels = []
    for i in range(height):
        for j in range(width):
            pixel = image.getpixel((j, i))
            pixels.append(pixel)
    return pixels

def grey_transform(pixels: Pixels) -> List[int]:
    result = list()
    for pxl in pixels:
        grey = math.floor((pxl[0] + pxl[1] + pxl[2])/3)
        result.append(grey)
    return result

def print_image(ascii_density: str, width: int, height: int, grey_pixels: List[int]) -> None:
    line = ""
    for value in grey_pixels:
        index = round(value*(len(ascii_density) - 1)/255)
        if len(line) >= width:
            print(line)
            line = ""
        line += ascii_density[index]

if __name__ == "__main__":
    ascii_density = "  .:-=+*#%@"
    img = Image.open("./dog.jpg")
    new_scaled = img.resize((128, 96))
    new_scaled.save("./dog_scaled.jpg")
    img.close()

    img_scaled = Image.open("./dog_scaled.jpg")
    width, height = img_scaled.size
    print(f"w: {width}, h: {height}")

    pixels = load_pixels(img_scaled)
    grey_values = grey_transform(pixels)

    print_image(ascii_density, width, height, grey_values)

    img_scaled.close()
