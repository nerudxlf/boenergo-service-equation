import pydantic


class SchemeEquation(pydantic.BaseModel):
    a: str
    b: str
    c: str
