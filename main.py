FILE_NAME = "storage.txt"

def load_tasks():
    """Load existing tasks from file."""
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks back to file."""
    # Write each task on a new line
    with open(FILE_NAME, "w") as file:
        file.write("\n".join(tasks))

def add_task(tasks):
    """Prompts for a new task and adds it to the list."""
    task = input("Enter a new task: ").strip()
    
    # Input validation
    if not task:
        print("Task cannot be empty! Please try again.")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    """Displays all tasks with 1-based indexing."""
    if not tasks:
        print("\n📝 No tasks available. Add one to get started!")
        return
    
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("-" * 20)

def delete_task(tasks):
    """Deletes a task by its number."""
    if not tasks:
        print("Nothing to delete. The task list is empty.")
        return
    
    # Display tasks before asking for choice
    view_tasks(tasks)
    
    try:
        choice = input("Enter task number to delete (or 0 to cancel): ")
        
        # Check for cancel option
        if choice == '0':
            print("Deletion cancelled.")
            return

        task_index = int(choice) - 1 # Convert to 0-based index
        
        # Check if index is within range
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("❌ Invalid task number! Please choose a number from the list.")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            add_task(tasks)
        elif option == "2":
            view_tasks(tasks)
        elif option == "3":
            delete_task(tasks)
        elif option == "4":
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("🚫 Invalid option. Please choose 1, 2, 3, or 4.")

# The corrected entry point for the script
if __name__ == "__main__":
    main()