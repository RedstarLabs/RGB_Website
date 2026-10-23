import pytest

from rgb_website.services import SurveyService


def test_invalid_color_id_is_not_stored(db_session) -> None:
    service = SurveyService(db_session)
    service.create_session("session-1", "1.0")
    session = service.get_session("session-1")
    assert session is not None
    color = service.get_next_color(session)
    assert color is not None

    with pytest.raises(ValueError):
        service.add_response(
            session_id="session-1",
            color_id="not-in-session",
            trial_number=1,
            emotion="Freude",
            experiment_version="1.0",
        )

    assert service.get_responses("session-1") == []
