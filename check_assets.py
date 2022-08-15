from os.path import exists

import yaml

with open("links.yaml", "r", encoding="utf8") as links_file:
    data = yaml.load(links_file, Loader=yaml.CLoader)

for category_name in data:
    for link in data[category_name]:
        if not exists("src/assets/icons/" + link["img"]):
            raise ValueError(f"File {link['img']} is missing from the assets directory")
