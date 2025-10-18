# ToDo CLI

A simple command-line ToDo list application written in Python. Tasks are stored as
JSON and can be managed with intuitive commands.

## Installation

Create and activate a virtual environment, then install the project in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Usage

The application installs a `todo` command. The default storage file lives at
`~/.todo_data.json`. You can override it with the `--storage` option.

```bash
# Add new tasks
$ todo add "Buy groceries"
Added task 1: Buy groceries

# List tasks
$ todo list
[✗] 1: Buy groceries

# Complete a task
$ todo complete 1
Completed task 1: Buy groceries

# Remove completed tasks
$ todo clear
Removed 1 completed task.

# Delete a task by id
$ todo delete 1
Deleted task 1: Buy groceries
```

## Running Tests

```bash
pytest
```
