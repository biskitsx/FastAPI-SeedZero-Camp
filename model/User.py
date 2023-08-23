from beanie import Document


class User(Document):
    name: str
    age: int | None = None
    marry: bool
