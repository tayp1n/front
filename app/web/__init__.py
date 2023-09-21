"""WEB API for app."""
try:
    # from app import init_settings

    # init_settings()
    from app.web.application import get_app
except Exception:
    raise


__all__ = ["get_app"]
