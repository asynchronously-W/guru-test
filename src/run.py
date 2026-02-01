from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka

from src.setup.app_factory import create_ioc_container, create_web_app
from src.setup.config.settings import create_settings
from src.setup.logging import configure_logging


def make_app() -> FastAPI:
    settings = create_settings()

    configure_logging(settings.logging.level)

    app = create_web_app()
    container = create_ioc_container(settings)

    setup_dishka(container, app)

    return app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app=make_app(),
        port=8000,
        reload=False,
        loop="uvloop"
    )
