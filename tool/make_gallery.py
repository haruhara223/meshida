from PIL import Image
import os

IMG_DIR = "../src/img/"
IMG_DIR_HTML = "../img/"
HTML_DIR = "../src/gallery/"
IMG_TEMPLATE_HTML = "          <div class=\"column\"><img src=\"{}\"></div>"
OPEN_COLUMN_HTML = "<div class=\"columns is-desktop\">"
END_COLUMN_HTML = "</div>"
COLUMN_TAMPLATE_HTML = "<div class=\"column\"></div>"

dir_list = os.listdir(IMG_DIR)

html_template = ""
with open('template.html') as f:
    html_template = f.read()

for d in dir_list:
    img_contents = []
    title = d
    img_contents.append(OPEN_COLUMN_HTML)
    for idx, img_path in enumerate(os.listdir(os.path.join(IMG_DIR, d))):
        if idx % 3 == 0 and idx > 0:
            img_contents.append(END_COLUMN_HTML)
            img_contents.append(OPEN_COLUMN_HTML)
        img_contents.append(IMG_TEMPLATE_HTML.format(os.path.join(IMG_DIR_HTML, d, img_path)))
    while idx % 3 != 2:
        img_contents.append(COLUMN_TAMPLATE_HTML)
        idx += 1
    img_contents.append(END_COLUMN_HTML)
    html = html_template.replace("%gallery%", "\n".join(img_contents))
    with open(os.path.join(HTML_DIR, d) + ".html", mode="w") as f:
        f.write(html)
    
    
    
