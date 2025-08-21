import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.writelines(task + "\n" for task in tasks)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks.pop(idx)
                    save_tasks(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
