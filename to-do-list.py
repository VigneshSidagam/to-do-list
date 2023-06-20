# TO-DO-LIST
def fun():
    tasks = []
    def add_tasks():
        task = input("Enter the task you wanna add...")
        tasks.append(task)
        print(f"\n{task} task added successfully")
    def display_tasks():
        if tasks:
            for i, j in enumerate(tasks, start=1):
                print(f"{i}.{j}")
            print("\n")
        else:
           print("\nNo tasks found...!\n")
    def remove_tasks():
        display_tasks()
        if tasks:
            index = int(input("Enter the index number of the task you wanna remove:"))-1
            if 0<=index<=len(tasks):
                remove = tasks.pop(index)
                print(f"\n{remove} task removed successfully")
            else:
                print("\nInvalid index number")
        else:
            print("\nNo tasks found")
    def clear_tasks():
        tasks.clear()
        print("\nAll tasks cleared successfully")
    while True:
        print("Your choices are:")
        print("1)Add Tasks")
        print("2)Display Tasks")
        print("3)Remove Tasks")
        print("4)Clear Tasks")
        print("5)Exit")
        choice = input("\n Enter your choice:")
        if choice == "1":
            add_tasks()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            remove_tasks()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Thank you for using To-Do-List")
        else:
            print("Invalid choice")
fun()
ask = input("Do you wanna use this To-Do-List again?").lower()
while ask!= "no":
    fun()
    ask = input("Do you wanna use this To-Do-List again?").lower()
else:
    print("Thank you")




        
