class MessengerError(Exception):
    def __init__(self, message=None, http_status=None):
        super(MessengerError, self).__init__(message)

        self.message = message
        self.http_status = http_status


class AuthKeyError(MessengerError):
    """
    Auth Key Not Provided
    """
    pass


class HttpMethodError(MessengerError):
    pass


class HttpError(MessengerError):
    pass


class DeadConversationError(MessengerError):
    """
    Raised when a conversation is dead.
    """
    pass


class SendAPIError(MessengerError):
    """

    """
    pass