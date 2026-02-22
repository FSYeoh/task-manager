tasks = []
import json
import os

FILENAME = "tasks.json"

# Load tasks if file exists
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

print("Welcome to Francis' Task Manager 🧠")

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_text = input("Enter task: ")
        tasks.append({"task": task_text, "done": False})
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {status} {task['task']}")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
        else:
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {status} {task['task']}")

            try:
                number = int(input("Enter task number to mark complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    print("Task marked complete!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {status} {task['task']}")

            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"Deleted: {removed['task']}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        with open(FILENAME, "w") as file:
            json.dump(tasks, file)
        print("Tasks saved. Goodbye 👋")
        break

    else:
        print("Invalid option")