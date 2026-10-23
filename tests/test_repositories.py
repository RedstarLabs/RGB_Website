from rgb_website.services import SurveyService


def test_sessions_and_responses_can_be_saved_and_read(db_session) -> None:
    service = SurveyService(db_session)
    service.create_session("session-1", "1.0")
    session = service.get_session("session-1")
    assert session is not None
    color = service.get_next_color(session)
    assert color is not None
    service.add_response(
        session_id="session-1",
        color_id=color.color_id,
        trial_number=1,
        emotion="Freude",
        experiment_version="1.0",
    )

    session = service.get_session("session-1")
    responses = service.get_responses("session-1")

    assert session is not None
    assert session.experiment_version == "1.0"
    assert len(responses) == 1
    assert responses[0].color_r == color.color_r
    assert responses[0].color_g == color.color_g
    assert responses[0].color_b == color.color_b
    assert responses[0].emotion == "Freude"
