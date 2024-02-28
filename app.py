import requests
import logging
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen


save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    
query = "Narendra Modi"
url = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

soup = soup.find_all("img")

soup = soup[1:]
print(len(soup))

for index, img in enumerate(soup):
    img_url = img["src"]
    img_data = urlopen(img_url).read()
    with open(f"{save_dir}{index}.jpg", "wb") as f:
        f.write(img_data)