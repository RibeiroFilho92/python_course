grocery_list = []
exit_app = False

while not exit_app:

    try:
        option = input("[i]nsert [d]elete [l]ist [e]xit: ")

        if option.lower() == "i":
            item = input("Item to add: ")
            grocery_list.append(item)

        elif option.lower() == "d":
            index_item_delete = input("Insert the item index: ")

            try:
                grocery_list.pop(int(index_item_delete))

            except:
                print("Invalid index.")

        elif option.lower() == "l":
            grocery_list_len = range(len(grocery_list))
            for ind in grocery_list_len:
                print(ind, grocery_list[ind])

        elif option.lower() == "e":
            exit_app = True

    except:
        print("Invalid input.")