from app import init_settings
from app.web import get_app

# init_settings()


def main() -> None:
    """Entrypoint of the application."""

    import settings

    app = get_app()
    app.run_server(
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        debug=settings.DEBUG,
    )


if __name__ == "__main__":
    main()
