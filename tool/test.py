import os

from PIL import Image

img_path = "../src/img/190505_13h_tochigi/D5xWqcBVUAUV9zQ.jpg"
img = Image.open(img_path)
img_resize = img.resize((img.width // 2, img.height // 2))
img_resize.save(img_path + ".jpg")

