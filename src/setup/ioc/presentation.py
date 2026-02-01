from dishka import Provider, Scope, from_context
from starlette.requests import Request


class PresentationProvider(Provider):
    scope = Scope.REQUEST

    request = from_context(Request)