from pydantic import BaseModel


class UserBody(BaseModel):
    name: str
    age: int | None = None
    marry: bool
