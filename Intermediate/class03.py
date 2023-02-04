def multi(*args):

    total = 1
    for value in args:
        total *= value

    return total

def odd_even(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(multi(1, 2, 3, 4, 5))

print(odd_even(10))
print(odd_even(5))