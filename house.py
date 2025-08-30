from functools import reduce

house_list=[
    {"address":"tehran","area":200,"price":1800,"description":"alavator,parking,warehouse"},
    {"address": "mashhad", "area": 300, "price": 2300, "description": "parking,warehouse"},
    {"address": "ahvaz", "area": 150, "price": 1300, "description": "alavator"},
    {"address": "karaj", "area": 220, "price": 2000, "description": "alavator,warehouse"},
    {"address": "shiraz", "area": 180, "price": 1500, "description": "alavator,parking"},
    {"address": "babol", "area": 310, "price": 2500, "description": "alavator,parking,warehouse"},
    {"address": "esfehan", "area": 80, "price": 1000, "description": "warehouse"},
    {"address": "ghom", "area": 320, "price": 2600, "description": "alavator,parking"},
    {"address": "tabriz", "area": 250, "price": 2250, "description": "parking"}
]


#یافتن خانه هایی که پارکینگ دارند
def parking(house):
    return house["description"]=="alavator,parking,warehouse" or house["description"]=="parking,warehouse" or house["description"]=="parking,warehouse"or house["description"]=="parking"

result = list(filter(parking, house_list))


# معیار مرتب سازی بر اساس نام شهر باشد
def name(house):
    return house["address"]

result = sorted(result, key=name)
print(result)
print("-"*30)

# جمع کل قیمت های خانه های دارای پارکینگ
def all_total(total, house):
    return total + house["price"]

total = reduce(all_total, result, 0)
print(total)