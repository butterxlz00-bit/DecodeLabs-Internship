# Project 1: To-Do List App

A simple command-line To-Do List application built in Python as part of the DecodeLabs Python Programming Internship.

## About This Project

This project focuses on understanding the fundamentals of Python lists.

The application allows users to:

* Add tasks to a list
* View all added tasks
* Exit the application

**Key skills:** Python lists, `append()`, `for` loops, functions, user input, and conditional statements.

## Features

* **Add tasks** — Users can enter and add new tasks to the list.
* **View tasks** — Displays all tasks currently stored in the list.
* **Empty task validation** — Prevents users from adding an empty task.
* **Exit** — Allows users to safely exit the application.

## Tech Stack

* Python 3
* No external dependencies

## Project Structure

```text
project_1_todo_list/
├── todo.py
└── README.md
```

* `todo.py` — Contains the main To-Do List application.
* `README.md` — Contains information about the project and instructions for running it.

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code.
3. Open the VS Code terminal.
4. Run the program:

```bash
python todo.py
```

5. Select an option from the menu.

## How It Works

The program starts with an empty list:

```python
tasks = []
```

When the user enters a task, the task is added to the list using `append()`:

```python
tasks.append(task)
```

The program checks whether the list is empty. If tasks are available, a `for` loop is used to go through the list and display each task:

```python
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

The program continues running until the user selects the Exit option.

This project demonstrates the basic **Storage → Process → Display** concept using a Python list.

## Author

Built as part of the DecodeLabs Python Programming Internship, Batch 2026.




