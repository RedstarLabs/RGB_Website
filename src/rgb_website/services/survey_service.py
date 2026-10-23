from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from rgb_website.models import Response, SurveySession
from rgb_website.repositories import ResponseRepository, SurveySessionRepository


class SurveyService:
    def __init__(self, db: Session) -> None:
        self.sessions = SurveySessionRepository(db)
        self.responses = ResponseRepository(db)
        self.db = db

    def create_session(
        self,
        session_id: str,
        experiment_version: str,
    ) -> SurveySession:
        survey_session = SurveySession(
            id=session_id,
            experiment_version=experiment_version,
        )
        try:
            self.sessions.add(survey_session)
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise
        return survey_session

    def add_response(
        self,
        *,
        session_id: str,
        trial_number: int,
        color_r: int,
        color_g: int,
        color_b: int,
        emotion: str,
        color_order: int,
        experiment_version: str,
    ) -> Response:
        response = Response(
            session_id=session_id,
            trial_number=trial_number,
            color_r=color_r,
            color_g=color_g,
            color_b=color_b,
            emotion=emotion,
            color_order=color_order,
            experiment_version=experiment_version,
        )
        try:
            self.responses.add(response)
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise
        return response

    def get_session(self, session_id: str) -> SurveySession | None:
        return self.sessions.get(session_id)

    def get_responses(self, session_id: str) -> list[Response]:
        return self.responses.get_for_session(session_id)
