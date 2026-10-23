from fastapi import FastAPI

from rgb_website.api import health_router
from rgb_website.api.experiment import router as experiment_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="ColorEmotionStudy",
        description=(
            "Datensparsame Forschungsanwendung zur Zuordnung von Farben und Emotionen."
        ),
        version="0.1.0",
    )
    app.include_router(health_router)
    app.include_router(experiment_router)
    return app


app = create_app()
