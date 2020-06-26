from bs4 import BeautifulSoup
import requests
import urllib.request
import random
import os
from io import BytesIO
from PIL import Image

# search = input("enter your image search: ")
# params = {"p": search}
url = "https://www.creativeshrimp.com/top-30-artworks-of-beeple.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.find_all("a", {"class":"lightbox"})

for items in links:
    href = items.get('href')

    img_name = random.randrange(1, 500)
    full_name = str(img_name) + '.jpg'

    urllib.request.urlretrieve(href, "./imagessave/"+full_name)

    print("loop break...." + href)


    # img_obj = requests.get(items.attrs["href"])
    # print("getting: ", items.attrs["href"])
    # title = items.attrs["href"].split("/")[-1]
    #
    # img = Image.open(BytesIO(img_obj.content))
    # img.save("./imagessave/" + title, img.formet)
    # print(title)
