import copy

product = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

new_product = [
    {**product, "price": round(product["price"] * 1.1, 2)}
    for product in copy.deepcopy(product)
]

# print(new_product)

product_ordered = sorted(
    copy.deepcopy(product),
    key = lambda prod: prod["name"]
)

# print(product_ordered)

product_ordered_by_price = sorted(
    copy.deepcopy(product),
    key = lambda prod : prod["price"]
)

print(product_ordered_by_price)

