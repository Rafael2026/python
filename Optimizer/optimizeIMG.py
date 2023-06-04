from PIL import Image # python -m pip install Pillow

import os

pictures = "/Users/<user>/OneDrive/Music/img/"

if __name__ == "__main__":
  
  for filename in os.listdir(pictures):

    name, extension = os.path.splitext(pictures + filename)

    if extension in [".jpg", ".jpeg", ".png", ".webp"]:
      img = Image.open(pictures + filename)
      img.save(pictures + filename, optimize=True, quality=75, format="webp")
      img.close()
