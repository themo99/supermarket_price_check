import re

prices = [3.50, 2.99, 5.25, 4.10]

sum_prices = round(sum(prices), 2) # get the total price

print(sum_prices) ## Q1


cheap_items = []

for i in range(len(prices)):
    if prices[i] < 4:
        cheap_items.append(prices[i]) # find cheap items

print(cheap_items)

nums = [1, 2, 2, 3, 3, 3] ## Q2

freq_list = []
num_list = []
pairings_dict = {}

for i in range(len(nums)):       # get a unique list of items
    if nums[i] not in num_list:
        num_list.append(nums[i])

for i in range(len(num_list)):               # find the frequency of each item
    pairings_dict[num_list[i]] = 0
    for j in range(len(nums)):
        if num_list[i] == nums[j]:
            pairings_dict[num_list[i]] += 1

print(pairings_dict) ## Q3

def price_check(price1, price2):
    """determine the price of item2 relative to item 1"""
    if price1 < price2:                                       # find the relative prices
        return f'${price1} is cheaper than ${price2}'
    elif price1 == price2:
        return f'The items are the same cost (${price1})'
    else:
        return f'${price1} is more expensive than ${price2}'
    
print(price_check(0.1, 0.1)) # Q4


items = ["milk", "bread", "milk", "eggs", "bread"]
# expected: ["milk", "bread", "eggs"]

unique_items = []

for item in items:                    # get a unique shopping list
    if item not in unique_items:
        unique_items.append(item)

print(unique_items) # Q5

nums2 = [1, 2, 3, 4]

running_total = [0] * len(nums2)

for i in range(len(nums2)):                  # get a running total as each item is added
    running_total[i] += sum(nums2[:i + 1])

print(running_total) # Q6

tricky_string = "$6.49 per kg"
return_price = ''

for letter in tricky_string:                                                # extract prices
    if letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return_price += letter

print(float(return_price)) # Q7

ugly_string = "  nz BEEF Mince  "
clean_string = ''

ugly_words = ugly_string.rsplit()  # normalize string
for word in ugly_words:
    word = word.capitalize()
    if word == 'Nz':
        word = 'NZ'
    clean_string += word + ' '

print(clean_string) # Q8

items2 = {
    "milk": 3.50,
    "bread": 2.99,
    "eggs": 6.20
}

items2_total = round(sum(items2.values()), 2)  # create a 'recipet'
items2['Total'] = items2_total

for product, price in items2.items():
    print(f'{product:<5} ${price:.2f}')     

#for set in items2:

paknsave = {"milk": 3.50, "bread": 2.99}
countdown = {"milk": 3.80, "bread": 1}
newworld = {"milk": 2, "bread": 3.40}
cheapest_products = paknsave
supermarket_dict = {}

for i in cheapest_products.keys():   # create a new dict pointing cheapest supermarket to products
    supermarket_dict[i] = 'paknsave'

for product, price in countdown.items():  # see if countdown is cheaper than pak n save
    for i, j in cheapest_products.items():
        if i == product and price < j:
            cheapest_products[i] = price
            supermarket_dict[product] = 'countdown'

for product, price in newworld.items():     # see if new world is the cheapest
    for i, j in cheapest_products.items():
        if i == product and price < j:
            cheapest_products[i] = price
            supermarket_dict[product] = 'new world'

for product, price in cheapest_products.items():
    print(f'{product:} → {supermarket_dict[product]} (${price:.2f})')   # Q10
