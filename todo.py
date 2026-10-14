tasks = []

while True:
    print("1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
        #Sadaf Iqbal