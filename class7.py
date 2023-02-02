# 01
number = input("Insert an intenger number: ")

try:
    number_to_int = int(number)

    if number_to_int % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except:
    print("Invalid number")

# 02

hour = input("Insert the current hour: ")

try:
    hour_to_int = int(hour)

    if hour_to_int > 0 and hour_to_int < 12:
        print("Good morning!")
    elif hour_to_int >= 12 and hour_to_int < 18:
        print("Good afternoon!")
    elif hour_to_int >= 18 and hour_to_int < 22:
        print("Good evening!")
    elif hour_to_int >= 22 and hour_to_int < 24:
        print("Good night!")
    else:
        print("Well...")

except:
    print("Invalid hour")