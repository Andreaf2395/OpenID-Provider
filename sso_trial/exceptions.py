class SsoException(Exception):
    def __init__(self, source, code, message):
        super().__init__(message)
        self._source = source
        self._code = code

    @property
    def code(self):
        return self._code
    @property
    def source(self):
        return self._source

class InvalidEntityException(SsoException):
    pass

class EntityDoesNotExistException(SsoException):
    pass
   
class NoLoggedException(SsoException):
    def __init__(self):
        super().__init__(source= 'authentication', code= 'required', message='Authentication Required')

class NoPermissionException(SsoException):
    def __init__(self):
        super().__init__(source= 'permission', code= 'denied', message='Permission denied')

class InternalServerException(SsoException):
    def __init__(self):
        super().__init__(source= 'server', code= 'internal_server_error', message='Internal Server Error')

