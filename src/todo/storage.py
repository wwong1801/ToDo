"""Persistence helpers for the ToDo application."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from .models import Task

DEFAULT_STORAGE_PATH = Path.home() / ".todo_data.json"


def load_tasks(storage_path: Path = DEFAULT_STORAGE_PATH) -> List[Task]:
    """Load tasks from *storage_path*.

    Missing files are treated as an empty list of tasks.
    """

    try:
        data = json.loads(storage_path.read_text())
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as exc:  # pragma: no cover - defensive branch
        raise ValueError(f"Invalid task data in {storage_path}") from exc

    return [Task.from_dict(item) for item in data]


def save_tasks(tasks: Iterable[Task], storage_path: Path = DEFAULT_STORAGE_PATH) -> None:
    """Persist *tasks* to *storage_path* as JSON."""

    serialized = [task.to_dict() for task in tasks]
    storage_path.write_text(json.dumps(serialized, indent=2) + "\n")
