
"""
A simple command-line To-Do List application.

Users can add tasks to a list and view all the tasks.
This project demonstrates the use of lists, append(), and for loops.
"""

# List used to store all the tasks
tasks = []


def show_menu():
    """Display the available options to the user."""
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Exit")


def add_task():
    """Ask the user for a task and add it to the tasks list."""
    task = input("\nEnter your task: ")


    # Check if the user entered an empty task
    if task.strip() =="":
        print("Task cannot be empty.")
    else:
        # Add the task to the list
        tasks.append(task)
        print("Task added successfully!!")


def view_task():
    """Display all the tasks stored in the list."""
    print("\n===== YOUR TASKS =====")


    # Check if the task list is empty
    if len(tasks) == 0:
        print("No tasks have been added yet.")
    else:
        # Loop through the list and display each task
        for number, task in enumerate(tasks, start=1):
            print(f"{number}.f{task}")


# Welcome message
print("Welcome to the To-Do List App!")


# Keep showing the menu until the user chooses to exit
while True:
    show_menu()
    choice = input("\nEnter your choice: ")

    if choice =="1":
        add_task()

    elif choice =="2":
        view_task()

    elif choice =="3":
        print("\nThank you for using the To-Do List App!!")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")