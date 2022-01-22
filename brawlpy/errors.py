class Errors(Exception):
    """The Base Class for all errors"""

    def __init__(self,code,message):
        pass

    def __str__(self):
        return self.message

class Forbidden(Errors):
    """Raised If you API key is invalid"""

    def __init__(self, code, url, message):
        self.code = code
        self.url = url
        self.message = message
        super().__init__(self.code, self.message)

class TagNotFoundError(Errors):
    """Raised when a invalid player or club tag is passed"""

    def __init__(self, code, **kwargs):
        self.code = code
        self.message = "An Invalid Tag has been passed!"
        self.reason = kwargs.pop('reason',None)
        self.invalid_characters = kwargs.pop('invalid_characters', [])
        if self.reason:
            self.message += ''.join(f"\n Reason : {self.reason}")
        elif self.invalid_characters:
            self.message += ''.join(f"\n Invalid characters : {self.invalid_characters}")
        super().__init__(self.code, self.message)

class RateLimitError(Errors):
    """Raised when the rate limit is reached."""

    def __init__(self, code, url):
        self.code = code
        self.url = url
        self.message = 'The rate limit has been reached.'
        super().__init__(self.code, self.message)

class UnexpectedError(Errors):
    """Raised if an unknown error has occured."""

    def __init__(self, url, code, text):
        self.code = code
        self.url = url
        self.message = f'An unexpected error has occured.\n{text}'
        super().__init__(self.code, self.message)

class ServerError(Errors):
    """Raised if the API is down."""

    def __init__(self, code, url):
        self.code = code
        self.url = url
        self.message = 'The API is down. Please be patient and try again later.'
        super().__init__(self.code, self.message)

class BrawlerNotFound(Errors):
    """Raised when Invalid brawlerID has been passed"""

    def __init__(self,code,id = None):
        self.code = code
        if id:
            self.message = 'Invalid ID passed! {}'.format(id)

        super().__init__(self.code, self.message)

class CountryNotFound(Errors):
    """Raised when Invalid countryCode has been passed"""

    def __init__(self,code,countryCode = None):
        self.code = code
        if id:
            self.message = 'Invalid countryCode passed! {}'.format(countryCode)

        super().__init__(self.code, self.message)