import requests as r
import os

URL = "https://www.gamerpower.com/api/giveaways?platform=pc&type=game"
DIV_FORMAT = """<div class="deal-container">
    <div class="deal-details">
      <h2 class="deal-title">{}</h2>
      <a href="{}" class="link-button">link</a>
    </div>
    <img class="deal-thumbnail" src="{}">
</div>
"""

data = r.get(URL).json()
text = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Deals</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
"""

for i in range(len(data)):
	text+=DIV_FORMAT.format(data[i]["title"],data[i]["open_giveaway"],data[i]["thumbnail"])

text+="""</body>
</html>"""


DIRECT = os.path.dirname(__file__)+"\\"


fil = open(DIRECT+"index.html","w")
fil.write(text)
fil.close()

os.startfile(DIRECT+"index.html")