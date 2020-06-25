from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image

search = input("enter your image search: ")
params = {"p": search}
r = requests.get("https://www.bing.com/images/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.find_all("a", {"class": "iusc"})

for items in links:
    img_obj = requests.get(items.attrs["href"])
    print("getting: ", items.attrs["href"])
    title = items.attrs["href"].split("/")[-1]

    img = Image.open(BytesIO(img_obj.content))
    img.save("./imagessave/" + title, img.formet)
    print(title)
