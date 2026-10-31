while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        with open("todo.txt", "a") as f:
            f.write(task + "\n")
        print("Task saved")

    elif choice == "2":
        try:
            with open("todo.txt", "r") as f:
                for line in f:
                    print("-", line.strip())
        except FileNotFoundError:
            print("No tasks yet")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
