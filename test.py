from string import ascii_letters, digits

from app.schemas.errors import *


def validate_password(password: str, ) -> None:
    if len(password) < 8:
        raise NotCorrectSizePassword('Password должен быть от 8 символов')
    if all(not x.isdigit() for x in password):
        raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")
    if all(not x.islower() for x in password):
        raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")
    if all(not x.isupper() for x in password):
        raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")

    test = ascii_letters + digits + '_!+-'
    for el in password:
        if el not in test:
            raise NotCorrectPassword("""Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-""")


validate_password('asdadasdA2')