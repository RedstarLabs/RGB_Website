import pytest
from sqlalchemy.exc import IntegrityError

from rgb_website.services import SurveyService


def test_invalid_rgb_value_is_not_stored(db_session) -> None:
    service = SurveyService(db_session)
    service.create_session("session-1", "1.0")

    with pytest.raises(IntegrityError):
        service.add_response(
            session_id="session-1",
            trial_number=1,
            color_r=256,
            color_g=75,
            color_b=101,
            emotion="Freude",
            color_order=1,
            experiment_version="1.0",
        )

    assert service.get_responses("session-1") == []
