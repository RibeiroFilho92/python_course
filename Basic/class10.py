name_list = ["Luke", "Lea", "Chewe", "Mando"]
name_list.append("Hunter")
name_list.append("Geralt")
name_list.pop()

indexes = range(len(name_list))

for name in indexes:

    print(name, name_list[name])

_, _, _, baddass, *_ = name_list

print("\n", baddass, "\n")

name_tuple = tuple(name_list)
# name_tuple.append() NOPE, they are immutable

name_enumerate = enumerate(name_tuple)

for ind, name in name_enumerate:

    print(ind, name)

# print(next(name_enumerate)) NOPE, it's "finished"
