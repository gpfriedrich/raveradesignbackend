from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Confirma que a API está respondendo, sem consultar o banco."""
    return {"status": "ok"}
