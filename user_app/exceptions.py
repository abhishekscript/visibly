
class BaseCustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return self.msg


class RecordNotFoundException(BaseCustomException):
    error_code = 'recordNotFound'
    error_message = 'Record not found for given id'


class UserApplicationNotFound(BaseCustomException):
    error_code = 'userAppNotFound'
    error_message = 'User application not found'


class UserApplicationAlreadyReserved(BaseCustomException):
    error_code = 'userAppReservedAlready'
    error_message = 'User application already reserved'
