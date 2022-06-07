import re
from fractions import Fraction

from fastapi import HTTPException, status

from src.routers.equation.service import service_solution
from src.schemes.scheme_equation import SchemeEquation, SchemeEquationAnswer


async def controller_solution(equation: SchemeEquation) -> SchemeEquationAnswer:
    """
    Checking for Errors and getting answer
    :param equation: ax^2 + bx + c = 0 (Current a, b and c numbers)
    :return: SchemeEquationAnswer:
    """
    a, b, c = equation.a, equation.b, equation.c
    if not a or a.isalpha() or b.isalpha() or c.isalpha():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Value Error")
    try:
        a = Fraction(a)
        b = Fraction(b if b else 0)
        c = Fraction(c if c else 0)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Value Error")
    answer = await service_solution(a, b, c)
    return answer


