"""Tests for the ToDo CLI."""

from __future__ import annotations

from pathlib import Path

import pytest

from todo.cli import parse_args, run_cli
from todo.storage import load_tasks


@pytest.fixture()
def storage_path(tmp_path: Path) -> Path:
    return tmp_path / "tasks.json"


def invoke(argv: list[str], storage_path: Path) -> str:
    args = parse_args(["--storage", str(storage_path), *argv])
    return run_cli(args)


def test_add_task_creates_entry(storage_path: Path) -> None:
    message = invoke(["add", "Buy milk"], storage_path)
    assert "Added task" in message

    tasks = load_tasks(storage_path)
    assert len(tasks) == 1
    assert tasks[0].description == "Buy milk"
    assert not tasks[0].completed


def test_list_returns_all_tasks(storage_path: Path) -> None:
    invoke(["add", "Task one"], storage_path)
    invoke(["add", "Task two"], storage_path)

    message = invoke(["list"], storage_path)
    assert "Task one" in message
    assert "Task two" in message


def test_complete_marks_task(storage_path: Path) -> None:
    invoke(["add", "Write tests"], storage_path)
    message = invoke(["complete", "1"], storage_path)

    assert "Completed task 1" in message
    tasks = load_tasks(storage_path)
    assert tasks[0].completed is True


def test_clear_removes_completed_tasks(storage_path: Path) -> None:
    invoke(["add", "Task one"], storage_path)
    invoke(["add", "Task two"], storage_path)
    invoke(["complete", "1"], storage_path)

    message = invoke(["clear"], storage_path)
    assert "Removed 1 completed task" in message

    tasks = load_tasks(storage_path)
    assert len(tasks) == 1
    assert tasks[0].description == "Task two"
