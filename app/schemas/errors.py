class NotUniqueUsername(Exception):
    """Username не униакльный"""


class NotCorrectSizeUsername(Exception):
    """Username должен быть от 3 до 30 символов"""


class NotCorrectUsername(Exception):
    """Username должен состоять только из латинских бук, цифр и _"""


class NotUniqueEmail(Exception):
    """Email не униакльный"""


class NotCorrectEmail(Exception):
    """Email не корректный"""


class NotCorrectSizePassword(Exception):
    """Password должен быть от 8 символов"""


class NotCorrectPassword(Exception):
    """Password должен включать минимум одну: заглваную букву, строчную букву, цифру.
    И состоять только из латинских бук, цифр и _!+-"""


class WrongPassword(Exception):
    """Неправильный пароль"""


class WrongEmail(Exception):
    """Неправильный email"""
