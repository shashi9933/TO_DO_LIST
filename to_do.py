# Empty list to store tasks
tasks = []

def show_menu():
    print("~~~ TO-DO LIST MENU ~~~")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("~~~ TASKS ~~~")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_completed():
    view_tasks()
    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index] = f"{tasks[task_index]} [Completed]"
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1

    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
