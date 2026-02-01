from dishka import Provider

from src.setup.ioc.application import ApplicationProvider
from src.setup.ioc.domain import DomainProvider
from src.setup.ioc.infrastructure import infrastructure_providers
from src.setup.ioc.presentation import PresentationProvider
from src.setup.ioc.settings import SettingsProvider


def get_providers() -> tuple[Provider, ...]:
    return (
        SettingsProvider(),
        DomainProvider(),
        ApplicationProvider(),
        *infrastructure_providers(),
        PresentationProvider(),
    )
