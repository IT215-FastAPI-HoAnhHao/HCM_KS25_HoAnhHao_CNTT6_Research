from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class AppException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message



class BadRequestException(AppException):
    def __init__(self, message: str = "Bad request"):
        super().__init__(400, message)


class ForbiddenException(AppException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(403, message)


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(404, message)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": {
                    "code": exc.status_code,
                    "message": exc.message
                }
            }
        )