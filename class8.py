name = "Jose Ribeiro"
str_name_asterisk = ""
aux = 0

while len(name) > aux:
    str_name_asterisk += "*" + name[aux]
    aux += 1

print(str_name_asterisk)