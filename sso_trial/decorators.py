from .exceptions import EntityDoesNotExistException, SsoException, InternalServerException, NoLoggedException, NoPermissionException, InvalidEntityException
from .serializers import SsoExceptionSerializer

exception_status_code_mapper = {
    EntityDoesNotExistException: 404,
    InternalServerException: 500,
    NoLoggedException: 401,
    NoPermissionException: 403,
    InvalidEntityException: 422,
}

def serialize_exceptions(func):
    def func_wrapper (*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except SsoException as e:
            body = SsoExceptionSerializer.serialize(e)
            status = exception_status_code_mapper[type(e)]
        return body, status
    return func_wrapper