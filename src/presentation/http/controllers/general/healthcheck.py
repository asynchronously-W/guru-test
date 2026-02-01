from fastapi import APIRouter


def create_healthcheck_router() -> APIRouter:
    router = APIRouter()

    @router.get("/healthcheck", tags=["General"])
    async def healthcheck() -> dict[str, str]:
        return {"status": "ok"}

    return router
