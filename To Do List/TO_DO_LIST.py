import datetime

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = []
            for line in file:
                task, status, time = line.strip().split("|")
                tasks.append({"task": task, "status": status, "time": time})
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['status']}|{t['time']}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["status"] == "done" else "❌"
        print(f"{i}. {t['task']} [{status}] (Added: {t['time']})")

def add_task(tasks):
    task = input("Enter new task: ")

    # Prevent duplicate
    for t in tasks:
        if t["task"].lower() == task.lower():
            print("Task already exists!")
            return

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"task": task, "status": "pending", "time": time})
    save_tasks(tasks)
    print("Task added!")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "done"
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def edit_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task name: ")

            # Prevent duplicate
            for t in tasks:
                if t["task"].lower() == new_task.lower():
                    print("Task already exists!")
                    return

            tasks[num - 1]["task"] = new_task
            save_tasks(tasks)
            print("Task updated!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def clear_all(tasks):
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ")
    if confirm.lower() == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks deleted!")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            clear_all(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()