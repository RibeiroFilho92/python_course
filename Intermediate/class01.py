def mine_sum(x, y):
    print(x + y)
    # return None

mine_sum(5, 5)

def mine_sub(x = 0, y = 0):
    print(x - y)

mine_sub(5)
mine_sub(9, 5)

def mine_mult(x, y=None):
    if y is None:
        print(x)
    else:
        print(x * y)

mine_mult(5)
mine_mult(9, 5)
