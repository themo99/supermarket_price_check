from bs4 import BeautifulSoup
import requests

url = "https://sandbox.oxylabs.io/products?_gl=1*9ypm4a*_gcl_au*MjAwOTg3OTA5Mi4xNzY4OTc4Njg0"
headers = {
    "User-Agent": "PriceChecker/1.0 (personal use)"
}

scrape_page = requests.get(url, headers=headers, timeout=20)
soup = BeautifulSoup(scrape_page.text, "html.parser")

titles = soup.findAll("h4", attrs={"class":"title css-7u5e79 eag3qlw7"})

for title in titles:
    print(title.text)