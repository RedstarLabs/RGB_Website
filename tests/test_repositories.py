from rgb_website.services import SurveyService


def test_sessions_and_responses_can_be_saved_and_read(db_session) -> None:
    service = SurveyService(db_session)
    service.create_session("session-1", "1.0")
    service.add_response(
        session_id="session-1",
        trial_number=1,
        color_r=217,
        color_g=75,
        color_b=101,
        emotion="Freude",
        color_order=1,
        experiment_version="1.0",
    )

    session = service.get_session("session-1")
    responses = service.get_responses("session-1")

    assert session is not None
    assert session.experiment_version == "1.0"
    assert len(responses) == 1
    assert responses[0].color_r == 217
    assert responses[0].emotion == "Freude"
