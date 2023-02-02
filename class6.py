name = input("Insert your name: ")
age = input("Insert your age: ")

if name and age:
    name_inverted = name[::-1]
    there_is_blank_spaces_in_name = " " in name;
    
    print(f"Your name is {name}")
    print(f"Your name inverted is {name_inverted}")
    
    if there_is_blank_spaces_in_name:
        print("Your hame has blank space(s)")
    else:
        print("Your hame hasn't blank space(s)")

    print(f"Your name has {len(name)} letters")
    print(f"The first letter of your name is {name[0]}")
    print(f"The last letter of your name is {name[-1]}")

else:
    print("Invalid input")
