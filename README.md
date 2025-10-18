# TickTick-lite

TickTick-lite is a minimal browser-only to-do application inspired by TickTick. It runs entirely in the browser, stores tasks in `localStorage`, and is ready for zero-config deployment on GitHub Pages.

## Features

- Add tasks with title, optional due date, priority (None/Low/Medium/High), and comma-separated tags.
- Filter views for All, Today, Upcoming, Overdue, and Completed tasks with live counts.
- Toggle completion, edit, or delete tasks directly from the list.
- Automatic sorting by completion state, due date, and creation time.
- Responsive, mobile-friendly layout for screens under 480px wide.

## Getting Started

1. Clone or download this repository.
2. Open `index.html` in any modern web browser.

No build tools or servers are required.

## Deploying to GitHub Pages

1. Push the repository to GitHub.
2. In the repository settings, open **Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select the branch to publish (e.g., `main`) and the `/root` directory.
5. Save the settings. Your site will be available at `https://<user>.github.io/<repo>/` shortly.

## Data Storage

Tasks persist in `localStorage` under the key `ttlite_tasks`. Clearing browser storage or switching devices will remove the tasks.

## License

MIT License.
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
