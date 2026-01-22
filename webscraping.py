from bs4 import BeautifulSoup
import requests

url = "https://sandbox.oxylabs.io/products?_gl=1*9ypm4a*_gcl_au*MjAwOTg3OTA5Mi4xNzY4OTc4Njg0"
headers = {
    "User-Agent": "PriceChecker/1.0 (personal use)"
}

scrape_page = requests.get(url, headers=headers, timeout=20)
soup = BeautifulSoup(scrape_page.text, "html.parser")

titles = soup.find_all("h4", attrs={"class":"title css-7u5e79 eag3qlw7"})
prices = soup.find_all("div", attrs={"class": "price-wrapper css-li4v8k eag3qlw4"})


for price, title in zip(prices, titles):
    clean_price = ""
    for letter in price.text:
        if letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',']:
            if letter == ',':
                letter = '.'
            clean_price += letter
    print(f"The price of {title.text} is €{clean_price}")
