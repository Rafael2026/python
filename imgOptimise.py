from PIL import Image # python -m pip install Pillow

import os

pictures = "/Users/rafaa/OneDrive/Music/imagenes/"

if __name__ == "__main__":
  
  for filename in os.listdir(pictures):

    name, extension = os.path.splitext(pictures + filename)

    if extension in [".jpg", ".jpeg", ".png", ".webp"]:
      music = Image.open(pictures + filename)
      music.save(pictures + filename, optimize=True, quality=75, format="webp")
      music.close()