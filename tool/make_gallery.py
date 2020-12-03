import os

IMG_DIR = "../src/img/"
IMG_DIR_HTML = "img/"
HTML_DIR = "../src"
IMG_TEMPLATE_HTML = "        <img src=\"{}\">"

dir_list = os.listdir(IMG_DIR)

html_template = ""
with open('template.html') as f:
    html_template = f.read()

for d in dir_list:
    img_contents = []
    title = d
    for img_path in os.listdir(os.path.join(IMG_DIR, d)):
        img_contents.append(IMG_TEMPLATE_HTML.format(os.path.join(IMG_DIR_HTML, d, img_path)))
    html = html_template.replace("%title%", title).replace("%gallery%", "\n".join(img_contents))
    with open(os.path.join(HTML_DIR, d) + ".html", mode="w") as f:
        f.write(html)
    
    
    
