from unittest.mock import Mock

import pytest

from app.models.users import UsersORM
from app.schemas.user_schemas import RegisterUser
from app.services.user import UserService


def test_list_tasks_returns_pydantic_models(
    service: UserService,
    repository_mock: Mock,
) -> None:
    # Имитируем, что метод get_all репозитория вернет эти задачи
    repository_mock.get_all.return_value = [
        UsersORM(id="task-1", title="Изучить pytest", completed=False),
        UsersORM(id="task-2", title="Написать первый тест", completed=True),
    ]

    result = service.list_tasks()

    assert result == [
        RegisterUser(id="task-1", title="Изучить pytest", completed=False),
        RegisterUser(id="task-2", title="Написать первый тест", completed=True),
    ]