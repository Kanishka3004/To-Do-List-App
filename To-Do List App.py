import json
import os

TODO_FILE = "todo_data.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks in your to-do list.")
    else:
        print("\n📋 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {status} {task['task']}")

def add_task(tasks):
    task_desc = input("Enter the task: ")
    tasks.append({"task": task_desc, "done": False})
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed = tasks.pop(task_num)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
