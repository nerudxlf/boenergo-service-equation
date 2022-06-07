import pydantic


class SchemeEquation(pydantic.BaseModel):
    a: str
    b: str
    c: str


class SchemeAnswer(pydantic.BaseModel):
    x1: float | None
    x2: float | None


class SchemeEquationAnswer(pydantic.BaseModel):
    status: str
    msg: str
    answer: SchemeAnswer

