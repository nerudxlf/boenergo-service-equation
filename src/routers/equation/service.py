import math
from fractions import Fraction

from src.schemes.scheme_equation import SchemeEquationAnswer, SchemeAnswer


async def service_solution(a: Fraction, b: Fraction, c: Fraction) -> SchemeEquationAnswer:
    """
    ax^2 + bx + c = 0
    D = b^2 - 4ac
    d = 0; x = (-b + sqrt(D))/2a
    d > 0; x1/2 = (-b +/- sqrt(D))/2a
    d < 0; Error (complex number?)
    :param a: rational number or integer or real number
    :param b: rational number or integer or real number
    :param c: rational number or integer or real number
    :return: SchemeEquationAnswer
    """
    x1, x2 = None, None
    d = b ** 2 - 4 * a * c
    if d < 0:
        status = "error"
        msg = "Уравнение не имеет действительных решений"
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        status = "ok"
        msg = f"Уравнение имеет 2 решения"
    else:
        x1 = -b / (2 * a)
        status = "ok"
        msg = f"Уравнение имеет 1 решение"
    return SchemeEquationAnswer(status=status, msg=msg, answer=SchemeAnswer(x1=x1, x2=x2))
