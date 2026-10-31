# task = input("Enter a task: ")
# with open("task.txt","a") as f:
#     f.write(task+"\n")
# print("task save ho gyaa")
# try:
#     with open ("todo" , "r") as f:
#         for line in f:
#             print("_",line.strip())
# except FileNotFoundError:
#            print("file not found")

while True:
    print("\n1. add Task ")
    print("2. view Tasks")
    print("3. close it")
    choice = input("Choice: ")

    if choice == "1":
     task = input("Enter a task: ")
     with open("todo.txt","a") as f:
        f.write(task+"\n")
     print("task save ho gya")

    elif choice == "2":
     try:
         with open("todo.txt", "r") as f:
            for line in f:
              print("-", line.strip())
     except FileNotFoundError:
        print("no task is added")
    elif choice == "3":
       break
    else :
       print("choice not found")