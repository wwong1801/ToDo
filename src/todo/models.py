"""Data models for the ToDo application."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class Task:
    """Represents a single to-do item."""

    id: int
    description: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the task to a dictionary."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Create a :class:`Task` instance from serialized data."""
        created_at = data.get("created_at")
        if isinstance(created_at, str):
            created_at_dt = datetime.fromisoformat(created_at)
        else:
            created_at_dt = datetime.utcnow()
        return cls(
            id=int(data["id"]),
            description=str(data["description"]),
            completed=bool(data.get("completed", False)),
            created_at=created_at_dt,
        )


def next_task_id(tasks: List[Task]) -> int:
    """Return the next available task identifier."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1
