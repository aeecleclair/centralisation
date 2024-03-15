import json
import os
import shutil

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

if os.path.exists("./dist"):
    shutil.rmtree("./dist")
os.mkdir("./dist")

# Build the index file with Jinja2
with open("links2.yaml", "r", encoding="utf8") as links_file:
    data = yaml.load(links_file, Loader=yaml.CLoader)

jinja_env = Environment(
    loader=FileSystemLoader("./src"), autoescape=select_autoescape()
)
other_pages = [{"link": page["link"], "name": page["name"]} for page in data]
for page in data:
    file_path = page["link"] + ".html"
    page_template = jinja_env.get_template("index2.html")
    page_render = page_template.render(links=page["children"], other_pages=other_pages)

    # Save the new index file
    with open("./dist/" + file_path, "w", encoding="utf8") as file:
        file.write(page_render)

# Copy the assets directory
shutil.copytree("./src/assets", "./dist/assets")

# Create a json endpoint for MyEcl
json = json.dumps(data, ensure_ascii=False)
with open("./dist/links.json", "w", encoding="utf8") as links_json_file:
    links_json_file.write(json)
