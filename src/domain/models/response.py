from typing import Any, List, Optional

from domain.enums.HttpStatus import HttpStatusCode

class Response:
    def __init__(
        self,
        code: HttpStatusCode,
        data: Optional[Any] = None,
        errors: Optional[List[str]] = None
    ):
        self.code = code.value
        self.data = data
        self.errors = errors or []

    @property
    def is_success(self):
        return not self.errors

    def to_dict(self):
        return {
            "data": self.data,
            "errors": self.errors if self.errors else None
        }

    @staticmethod
    def success(code: HttpStatusCode, data: Any = None):
        if code.value < 200 or code.value >= 300:
            raise ValueError("Código de sucesso deve estar entre 200 e 299")
        return Response(code, data)

    @staticmethod
    def error(code: HttpStatusCode, errors: List[str]):
        if code.value < 400 or code.value >= 600:
            raise ValueError("Código de erro deve estar entre 400 e 599")
        return Response(code, None, errors)
