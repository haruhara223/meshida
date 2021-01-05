import os
from PIL import Image

IMG_DIR = "../src/img/"
TOP_IMG_BIG_FILE_NAME = "topimg_big.jpg"
TOP_IMG_FILE_NAME = "topimg.jpg"

dir_list = os.listdir(IMG_DIR)

for d in dir_list:
    if d == "不明": continue
    if not os.path.isdir(os.path.join(IMG_DIR, d)): continue
    img_contents = []
    for img_file_name in os.listdir(os.path.join(IMG_DIR, d)):
        if img_file_name in (TOP_IMG_BIG_FILE_NAME, TOP_IMG_FILE_NAME): continue
        img = Image.open(os.path.join(IMG_DIR, os.path.join(d, img_file_name)))
        if max(img.width, img.height) >= 850:
            scale_rate = max(img.width, img.height) / 800
            img_resize = img.resize((int(img.width // scale_rate), int(img.height // scale_rate)))
            img_resize.save(os.path.join(IMG_DIR, os.path.join(d, img_file_name)))

