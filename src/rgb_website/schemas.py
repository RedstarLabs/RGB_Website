from pydantic import BaseModel, ConfigDict, Field

from rgb_website.experiment import PALETTE_VERSION, Emotion


class ColorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str = Field(min_length=1, max_length=32)
    red: int = Field(ge=0, le=255)
    green: int = Field(ge=0, le=255)
    blue: int = Field(ge=0, le=255)
    position: int = Field(ge=1, le=10)


class ExperimentStateResponse(BaseModel):
    session_id: str
    status: str
    answered_count: int = Field(ge=0, le=10)
    total_count: int = 10
    next_color: ColorResponse | None
    experiment_version: str = PALETTE_VERSION


class StartExperimentResponse(ExperimentStateResponse):
    pass


class SubmitResponseRequest(BaseModel):
    color_id: str = Field(min_length=1, max_length=32)
    emotion: Emotion
    trial_number: int = Field(ge=1, le=10)
    experiment_version: str = Field(min_length=1, max_length=32)


class SubmitResponseResult(ExperimentStateResponse):
    accepted: bool = True
