exit = False
tasks = []
logs = []

while not exit:

    print("Commands: show, undo, redo")
    task = input("Insert one task: ")

    if task.lower() == "exit":
        
        exit = True
    elif task.lower() == "show":
        
        print("\nTASKS: \n")
        for t in tasks:
            print(t)
    elif task.lower() == "undo":

        tasks.pop()
    elif task.lower() == "redo":

        difference = len(logs) - len(tasks)
        if difference != 0:
            tasks.append(logs[difference * - 1])
    else:
        tasks.append(task)
        logs.append(task)

    print()
