def display_menu():
    print("===== To-Do List Menu =====")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. View all tasks")
    print("4. Quit")


def add_task(todo_list):
    task_description = input("Enter a task description: ")
    task = [task_description, False]
    todo_list.append(task)
    print(f'Task "{task_description}" added successfully!')


def mark_completed(todo_list):
    display_tasks(todo_list)
    index = int(input("Enter the index of the task to mark as completed: "))

    if 0 <= index < len(todo_list):
        todo_list[index][1] = True
        print("Task marked as completed!")
    else:
        print("Invalid index. Please try again.")


def display_tasks(todo_list):
    print("\n===== Tasks =====")
    for i, task in enumerate(todo_list):
        status = "[X]" if task[1] else "[ ]"
        print(f"{i}. {status} {task[0]}")


def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_completed(todo_list)
        elif choice == '3':
            display_tasks(todo_list)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
