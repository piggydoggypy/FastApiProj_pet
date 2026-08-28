from unittest.mock import Mock

import pytest
from datetime import datetime
from app.models.users import UsersORM
from app.schemas.user_schemas import RegisterUser, ResponseUser
from app.services.user import UserService


def test_create_user_commits_create_user(
    service: UserService,
    db_mock: Mock,
    repository_mock: Mock,
) -> None:
    created_task = UsersORM(id="1", username="user", email="email@gmail.com",
                            password="Password123",role="EMPLOYEE",
                            created_at="12.12.23")
    repository_mock.create_user.return_value = created_task
    repository_mock.get_all_usernames.return_value = ['ad', 'assdfff']
    repository_mock.get_all_emails.return_value = ['ad', 'assdfff']
    repository_mock.get_by_email.return_value = UsersORM(id="1", username="user", email="email@gmail.com",
                            password="Password123",role="EMPLOYEE",
                            created_at="12.12.23")

    result = service.create_user(RegisterUser(username="user", email="email@gmail.com", password="Password123"))

    assert result.username == "user"
    assert result.email == "email@gmail.com"
    assert result.id == "1"
    assert result.role == "EMPLOYEE"

    db_mock.commit.assert_called_once_with()
    assert result.model_dump() == {"id": "1", "username": "user", "email": "email@gmail.com", "role": "EMPLOYEE"}