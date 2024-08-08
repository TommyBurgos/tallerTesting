# to_do_list_manager.py

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {status}"

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"\nTask {idx}:")
            print(task)
            print('-' * 40)

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared.")

def main():
    manager = ToDoListManager()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (Low/Medium/High): ")
            task = Task(title, description, due_date, priority)
            manager.add_task(task)
            print("Task added successfully.")
        
        elif choice == '2':
            manager.list_tasks()
        
        elif choice == '3':
            manager.list_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            manager.mark_task_completed(task_number)
        
        elif choice == '4':
            manager.clear_tasks()
        
        elif choice == '5':
            print("Exiting To-Do List Manager.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
