import os

IMG_DIR = "../src/img/"
IMG_DIR_HTML = "../img/"
HTML_DIR = "../src/gallery/"
IMG_TEMPLATE_HTML = "          <div class=\"column\"><img src=\"{}\"></div>"
OPEN_COLUMN_HTML = "        <div class=\"columns is-desktop\">"
END_COLUMN_HTML = "        </div>"
COLUMN_TAMPLATE_HTML = "          <div class=\"column\"></div>"
TOP_IMG_BIG_FILE_NAME = "topimg_big.jpg"
TOP_IMG_FILE_NAME = "topimg.jpg"

dir_list = os.listdir(IMG_DIR)

html_template = ""
with open('template.html') as f:
    html_template = f.read()

for d in dir_list:
    img_contents = []
    img_num = 0
    img_contents.append(OPEN_COLUMN_HTML)
    for img_file_name in os.listdir(os.path.join(IMG_DIR, d)):
        if img_file_name in (TOP_IMG_BIG_FILE_NAME, TOP_IMG_FILE_NAME): continue
        if img_num % 3 == 0 and img_num > 0:
            img_contents.append(END_COLUMN_HTML)
            img_contents.append(OPEN_COLUMN_HTML)
        img_contents.append(IMG_TEMPLATE_HTML.format(os.path.join(IMG_DIR_HTML, d, img_file_name)))
        img_num += 1
    while img_num % 3 != 0:
        img_contents.append(COLUMN_TAMPLATE_HTML)
        img_num += 1
    img_contents.append(END_COLUMN_HTML)
    html = html_template.replace("%topimg%", os.path.join(IMG_DIR_HTML, d, TOP_IMG_BIG_FILE_NAME)).replace("%gallery%", "\n".join(img_contents))
    with open(os.path.join(HTML_DIR, d) + ".html", mode="w") as f:
        f.write(html)
