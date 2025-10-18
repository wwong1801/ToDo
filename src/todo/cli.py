"""Command-line interface for the ToDo application."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List

from .models import Task, next_task_id
from .storage import DEFAULT_STORAGE_PATH, load_tasks, save_tasks


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description="Simple ToDo list manager")
    parser.add_argument(
        "--storage",
        type=Path,
        default=DEFAULT_STORAGE_PATH,
        help=f"Path to the storage file (default: {DEFAULT_STORAGE_PATH})",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    subparsers.add_parser("list", help="List tasks")

    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("task_id", type=int, help="Identifier of the task to complete")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Identifier of the task to delete")

    subparsers.add_parser("clear", help="Remove all completed tasks")

    return parser.parse_args(argv)


def handle_add(tasks: List[Task], description: str) -> Task:
    """Add a task and return it."""
    task = Task(id=next_task_id(tasks), description=description)
    tasks.append(task)
    return task


def handle_complete(tasks: List[Task], task_id: int) -> Task:
    """Mark *task_id* as completed."""
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise ValueError(f"Task with id {task_id} not found")


def handle_delete(tasks: List[Task], task_id: int) -> Task:
    """Delete *task_id* from the task list."""
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
    raise ValueError(f"Task with id {task_id} not found")


def handle_clear(tasks: List[Task]) -> List[Task]:
    """Return a list containing only active tasks."""
    return [task for task in tasks if not task.completed]


def format_task(task: Task) -> str:
    """Return a human-readable representation of *task*."""
    status = "✓" if task.completed else "✗"
    return f"[{status}] {task.id}: {task.description}"


def run_cli(args: argparse.Namespace) -> str:
    """Execute the CLI command described by *args* and return the output string."""
    storage_path = args.storage
    tasks = load_tasks(storage_path)

    if args.command == "add":
        task = handle_add(tasks, args.description)
        save_tasks(tasks, storage_path)
        return f"Added task {task.id}: {task.description}"

    if args.command == "list":
        if not tasks:
            return "No tasks found."
        return "\n".join(format_task(task) for task in tasks)

    if args.command == "complete":
        task = handle_complete(tasks, args.task_id)
        save_tasks(tasks, storage_path)
        return f"Completed task {task.id}: {task.description}"

    if args.command == "delete":
        task = handle_delete(tasks, args.task_id)
        save_tasks(tasks, storage_path)
        return f"Deleted task {task.id}: {task.description}"

    if args.command == "clear":
        active_tasks = handle_clear(tasks)
        save_tasks(active_tasks, storage_path)
        removed = len(tasks) - len(active_tasks)
        return f"Removed {removed} completed task{'s' if removed != 1 else ''}."

    raise RuntimeError(f"Unsupported command: {args.command}")


def main(argv: Iterable[str] | None = None) -> None:
    """Entry point for the CLI application."""
    args = parse_args(argv)
    output = run_cli(args)
    print(output)


__all__ = [
    "DEFAULT_STORAGE_PATH",
    "Task",
    "format_task",
    "handle_add",
    "handle_clear",
    "handle_complete",
    "handle_delete",
    "main",
    "parse_args",
    "run_cli",
]
