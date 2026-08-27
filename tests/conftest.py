from unittest.mock import Mock

import pytest
from sqlalchemy.orm import Session

from app.repository.user import UserRepository
from app.services.user import UserService


@pytest.fixture
def db_mock() -> Mock:
    """Создаём мок сессии БД один раз и переиспользуем в тестах"""
    return Mock(spec=Session)

@pytest.fixture
def repository_mock() -> Mock:
    """Создаём мок UserRepository один раз и переиспользуем в тестах"""
    return Mock(spec=UserRepository)

@pytest.fixture
def service(db_mock: Mock, repository_mock: Mock) -> UserService:
    """Создаём UserService один раз, чтобы переиспользовать в тестах"""
    user_service = UserService(db_mock)
    user_service.user_repository = repository_mock
    return user_service
