from pydantic import BaseModel

class RunningFrequencyResponse(BaseModel):
    frquency: int
    reasoning: str