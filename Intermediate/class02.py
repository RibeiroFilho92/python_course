x = 1

def alter_x():

    global x # Bad practice
    x = 10
    print(x)

def alter_x_only_inside():
    
    x = 20


print(x)
alter_x()
alter_x_only_inside()
print(x)