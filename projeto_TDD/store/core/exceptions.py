class BaseException(Exception):
    message: str = 'internal server error'
    def __init__(self, message : str | None=None) -> None:
        if message:
            self.message = message

class NotFoundException(BaseException):
    message = 'not found'



