from gestor import Task, TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark as Completed")
        print("5. Exit")
        option = input("Select an option: ")

        if option == "1":
            task_name = input()
            manager.add_task(task_name)
        elif option == "2":
            manager.view_tasks()
            index = int(input())
            manager.remove_task(index)
        elif option == "3":
            manager.view_tasks()
        elif option == "4":
            manager.view_tasks()
            index = int(input())
            manager.mark_task_completed(index)
        elif option == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

