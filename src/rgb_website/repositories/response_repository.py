from sqlalchemy import func, select
from sqlalchemy.orm import Session

from rgb_website.models import Response


class ResponseRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add(self, response: Response) -> Response:
        self.db.add(response)
        self.db.flush()
        return response

    def get_for_session(self, session_id: str) -> list[Response]:
        statement = (
            select(Response)
            .where(Response.session_id == session_id)
            .order_by(Response.trial_number)
        )
        return list(self.db.scalars(statement))

    def count_for_session(self, session_id: str) -> int:
        return (
            self.db.scalar(
                select(func.count(Response.id)).where(Response.session_id == session_id)
            )
            or 0
        )
