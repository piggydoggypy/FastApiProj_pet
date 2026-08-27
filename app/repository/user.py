from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.users import UsersORM


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[UsersORM]:
        return list(self.db.scalars(select(UsersORM)).all())

    def get_by_id(self, id: str) -> UsersORM:
        return self.db.get(UsersORM, id)

    def get_by_email(self, email: str) -> UsersORM:
        return self.db.scalars(select(UsersORM).where(UsersORM.email == email)).first()

    def create_user(self, user: UsersORM) -> None:
        self.db.add(user)

    def delete_user(self, user: UsersORM) -> None:
        self.db.delete(user)

    def get_all_usernames(self) -> set[str]:  # поменять на поиск в дб where
        return set(self.db.scalars(select(UsersORM.username)).all())

    def get_all_emails(self) -> set[str]:
        return set(self.db.scalars(select(UsersORM.email)).all())

    def change_username(self, user_id: str, new_username: str) -> None:
        user = self.db.get(UsersORM, user_id)

        if user:
            user.username = new_username

    def change_password(self, user_id: str, new_password: str) -> None:
        user = self.db.get(UsersORM, user_id)

        if user:
            user.password = new_password
