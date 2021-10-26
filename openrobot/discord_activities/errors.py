import typing
import aiohttp

class DiscordActivityException(Exception):
    """The base discord activity exception."""

class UnexpectedHTTPResponse(DiscordActivityException):
    def __init__(self, response: aiohttp.ClientResponse, data: typing.Any):
        self.response = response
        self.data = data

        super().__init__(response, data)