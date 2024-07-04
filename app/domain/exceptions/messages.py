from dataclasses import dataclass

@dataclass(eq=False)
class ApplicationException(Exception):
    @property
    def message(self):
        return 'Произошла ошибка приложения'
@dataclass(eq=False)
class TextTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Слишком длинный текст сообщения "{self.text[:255]}..."'

@dataclass(eq=False)
class EmptyTextError(ApplicationException):
    @property
    def message(self):
        return 'Текст не может быть пустым'


@dataclass(eq=False)
class ApplicationException(Exception):
    @property
    def message(self):
        return 'Произошла ошибка приложения'