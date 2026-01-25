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



url_2 = "https://grosave.co.nz/search?page=3&storeId=172&storeId=365"

grosave_page = requests.get(url_2, headers=headers, timeout=20)
grosave_soup = BeautifulSoup(grosave_page.text, "html.parser")


grocery_titles = grosave_soup.find_all("span", class_='font-semibold text-gray-800 text-sm md:text-base leading-snug capitalize line-clamp-3 md:line-clamp-2 min-h-[2.5rem] md:min-h-[3rem]')
grocery_prices = grosave_soup.find_all("span", class_='text-md md:text-lg font-bold text-green-500 ')

print(grosave_soup)

for grocery_title in grocery_titles:
    print(f"{grocery_title.text} ")


import requests, re, json
from bs4 import BeautifulSoup

url = "https://grosave.co.nz/search?page=3&storeId=172&storeId=365"
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers, timeout=(5, 20))
soup = BeautifulSoup(r.text, "html.parser")

# 1. Find the Remix state script
script = next(
    s.string for s in soup.find_all("script")
    if s.string and "window.__remixContext" in s.string
)

# 2. Extract JSON
match = re.search(r"window\.__remixContext\s*=\s*({.*})", script, re.DOTALL)
remix = json.loads(match.group(1))

# 3. Pull products
products = remix["state"]["loaderData"]["routes/search"]["loaderSearchResults"]

# 4. Flatten to rows
rows = []
for p in products:
    for store, info in p["price_details"].items():
        rows.append({
            "product": p["name"],
            "store": store,
            "price": info["price"],
            "unit": info["unit"],
            "price_per_unit": info["price_per_unit"]
        })

for row in rows[:10]:
    print(row)

