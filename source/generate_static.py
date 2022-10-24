from json import load as load_json
from jinja2 import Template
from os import system

config = load_json(open("config.json", mode="r", encoding="utf-8"))
with open(config["main_template"], mode="r", encoding="utf-8") as f: baset = Template(f.read())

class MenuItem:
	def __init__(self, href, name):
		self.href = href
		self.name = name
menu = []
for item in config["articles"]:
	try:
		item["isindex"]
		assert item["isindex"] == True
	except KeyError:
		menu.append(MenuItem(item["filename"], item["article-name"]))
	except AssertionError:
		menu.append(MenuItem(item["filename"], item["article-name"]))

for item in config["articles"]:
	try:
		item["isindex"]
		isindex = item["isindex"]
	except KeyError:
		isindex = False
	with open("articles/" + item["filename"], mode="r", encoding="utf-8") as f: article = f.read()
	out = baset.render(article_name=item["article-name"], style_suffix=item["style-suffix"],
		isindex=isindex, menu=menu, article=article)
	with open("../" + item["filename"], mode="w", encoding="utf-8") as f: f.write(out)

for static in config["static"]:
	system("cp -R " + static + " ../" + static)