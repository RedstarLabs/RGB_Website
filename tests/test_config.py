from rgb_website.config import Settings


def test_settings_can_be_loaded_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("APP_PORT", "9000")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")

    settings = Settings()

    assert settings.app_env == "test"
    assert settings.app_port == 9000
    assert settings.database_url == "sqlite:///./test.db"
