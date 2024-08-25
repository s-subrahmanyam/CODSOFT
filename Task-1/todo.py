tasks = []

def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(index):
    global tasks
    try:
        # Convert index to zero-based index
        index = int(index) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print(f"Task number '{index + 1}' not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
            index = input("Enter the task number to remove: ")
            remove_task(index)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
