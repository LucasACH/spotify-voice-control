class BadRequest(Exception):
    """Bad Request - The request could not be understood by the server due to malformed syntax."""

    def __init__(self):
        super().__init__("Bad Request - The request could not be understood by the server due to malformed syntax.")


class Unauthorized(Exception):
    """Unauthorized - The request requires user authentication or, if the request included authorization credentials, authorization has been refused for those credentials."""

    def __init__(self):
        super().__init__("Unauthorized - The request requires user authentication or, if the request included authorization credentials, authorization has been refused for those credentials.")


class Forbidden(Exception):
    """Forbidden - The server understood the request, but is refusing to fulfill it."""

    def __init__(self):
        super().__init__("Forbidden - The server understood the request, but is refusing to fulfill it.")


class NotFound(Exception):
    """Not Found - The requested resource could not be found. This error can be due to a temporary or permanent condition."""

    def __init__(self):
        super().__init__("Not Found - The requested resource could not be found. This error can be due to a temporary or permanent condition.")


class TooManyRequests(Exception):
    """Too Many Requests - Rate limiting has been applied."""

    def __init__(self):
        super().__init__("Too Many Requests - Rate limiting has been applied.")


class InternalServerError(Exception):
    """Internal Server Error. You should never receive this error because our clever coders catch them all … but if you are unlucky enough to get one, please report it to us through a comment at the bottom of this page."""

    def __init__(self):
        super().__init__("Internal Server Error. You should never receive this error because our clever coders catch them all … but if you are unlucky enough to get one, please report it to us through a comment at the bottom of this page.")


class BadGateway(Exception):
    """Bad Gateway - The server was acting as a gateway or proxy and received an invalid response from the upstream server."""
    def __init__(self):
        super().__init__("Bad Gateway - The server was acting as a gateway or proxy and received an invalid response from the upstream server.")


class ServiceUnavailable(Exception):
    """Service Unavailable - The server is currently unable to handle the request due to a temporary condition which will be alleviated after some delay. You can choose to resend the request again."""
    def __init__(self):
        super().__init__("Service Unavailable - The server is currently unable to handle the request due to a temporary condition which will be alleviated after some delay. You can choose to resend the request again.")



def check_for_errors(status_code):
    if status_code == 400:
        raise BadRequest()
    elif status_code == 401:
        raise Unauthorized()
    elif status_code == 403:
        raise Forbidden()
    elif status_code == 404:
        raise NotFound()
    elif status_code == 429:
        raise TooManyRequests()
    elif status_code == 500:
        raise InternalServerError()
    elif status_code == 502:
        raise BadGateway()
    elif status_code == 503:
        raise ServiceUnavailable()
    else:
        return True