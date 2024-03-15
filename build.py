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

print(data)
jinja_env = Environment(
    loader=FileSystemLoader("./src"), autoescape=select_autoescape()
)
page_template = jinja_env.get_template("index3.html")
page_render = page_template.render(pages=data)

# Save the new index file
with open("./dist/index.html", "w", encoding="utf8") as file:
    file.write(page_render)

# Copy the assets directory
shutil.copytree("./src/assets", "./dist/assets")

# Create a json endpoint for MyEcl
json = json.dumps(data, ensure_ascii=False)
with open("./dist/links.json", "w", encoding="utf8") as links_json_file:
    links_json_file.write(json)
