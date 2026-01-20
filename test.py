prices = [3.50, 2.99, 5.25, 4.10]

sum_prices = round(sum(prices), 2)

print(sum_prices) ## Q1


cheap_items = []

for i in range(len(prices)):
    if prices[i] < 4:
        cheap_items.append(prices[i])

print(cheap_items)

nums = [1, 2, 2, 3, 3, 3] ## Q2

freq_list = []
num_list = []
pairings_dict = {}

for i in range(len(nums)):
    if nums[i] not in num_list:
        num_list.append(nums[i])

for i in range(len(num_list)):
    pairings_dict[num_list[i]] = 0
    for j in range(len(nums)):
        if num_list[i] == nums[j]:
            pairings_dict[num_list[i]] += 1

print(pairings_dict) ## Q3

def price_check(price1, price2):
    """determine the price of item2 relative to item 1"""
    if price1 < price2:
        return f'${price1} is cheaper than ${price2}'
    elif price1 == price2:
        return f'The items are the same cost (${price1})'
    else:
        return f'${price1} is more expensive than ${price2}'
    
print(price_check(0.1, 0.1)) # Q4


items = ["milk", "bread", "milk", "eggs", "bread"]
# expected: ["milk", "bread", "eggs"]

unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items) # Q5

nums2 = [1, 2, 3, 4]

running_total = [0] * len(nums2)

for i in range(len(nums2)):
    running_total[i] += sum(nums2[:i + 1])

print(running_total) # Q5

tricky_string = "$6.49 per kg"
price = tricky_string.replace(/\D/g,'');

print(price)