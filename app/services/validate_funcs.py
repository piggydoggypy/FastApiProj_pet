from re import match
from string import ascii_letters, digits

from app.schemas.errors import *


def validate_username(username: str, usernames: set[str]) -> None:
    if username in usernames:
        print(username, usernames)
        raise NotUniqueUsername("Username не униакльный")

    if not (3 <= len(username) <= 30):
        raise NotCorrectSizeUsername("Username должен быть от 3 до 30 символов")

    test = ascii_letters + digits + "_"
    for el in username:
        if el not in test:
            raise NotCorrectUsername(
                "Username должен состоять только из латинских бук, цифр и _"
            )


def validate_email(email: str, emails: set[str]) -> None:

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not match(pattern, email):
        raise NotCorrectEmail("Email не корректный")

    if email in emails:
        # Поднимать ошибку, что-то делать
        raise NotUniqueEmail("Email не униакльный")


def validate_password(
    password: str,
) -> None:
    if len(password) < 8:
        raise NotCorrectSizePassword("Password должен быть от 8 символов")
    if all(not x.isdigit() for x in password):
        raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")
    if all(not x.islower() for x in password):
        raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")
    if all(not x.isupper() for x in password):
        raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")

    test = ascii_letters + digits + "_!+-"
    for el in password:
        if el not in test:
            raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")
