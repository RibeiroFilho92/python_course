my_list = [n for n in range(10)]
# print(my_list)

my_list = [(x, y) for x in range(5) for y in range(5)]
# print(my_list)

product = {
    "name": "pen",
    "price": 2
}

my_product = {k : v for k, v in product.items()}
# print(my_product)

my_generator = (n for n in range(10000))

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator)) # 4, and so on... until 10000