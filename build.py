import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

with open("links.json", "r", encoding="utf8") as links_file:
    data = yaml.load(links_file, Loader=yaml.CLoader)

jinja_env = Environment(
    loader=FileSystemLoader("./templates"), autoescape=select_autoescape()
)
index_template = jinja_env.get_template("index.html")
index_render = index_template.render(links=data)

with open("dist/index.html", "w", encoding="utf8") as file:
    file.write(index_render)
