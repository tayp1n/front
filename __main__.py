import uvicorn
from app import init_settings


init_settings()


def main() -> None:
    """Entrypoint of the application."""

    import settings

    uvicorn.run(
        "app.web:get_app",
        workers=settings.WORKERS_COUNTS,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.RELOAD,
        factory=True,
    )


if __name__ == "__main__":
    main()
