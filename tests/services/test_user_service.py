from unittest.mock import Mock

import pytest

from app.models.users import UsersORM
from app.schemas.user_schemas import U, TaskUpdate
from app.services.task import TaskNotFoundError, TaskService


def test_list_tasks_returns_pydantic_models(
    service: TaskService,
    repository_mock: Mock,
) -> None:
    # Имитируем, что метод get_all репозитория вернет эти задачи
    repository_mock.get_all.return_value = [
        TaskORM(id="task-1", title="Изучить pytest", completed=False),
        TaskORM(id="task-2", title="Написать первый тест", completed=True),
    ]

    result = service.list_tasks()

    assert result == [
        TaskRead(id="task-1", title="Изучить pytest", completed=False),
        TaskRead(id="task-2", title="Написать первый тест", completed=True),
    ]