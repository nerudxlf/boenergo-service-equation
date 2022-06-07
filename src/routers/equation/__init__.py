from fastapi import APIRouter

from src.routers.equation.controller import controller_solution
from src.schemes.scheme_equation import SchemeEquation, SchemeEquationAnswer

router = APIRouter(
    prefix='/api/equation',
    tags=["equation"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=SchemeEquationAnswer)
async def solution(equation: SchemeEquation):
    """
    Route to obtain a solution to the quadratic equation
    :param equation: params a: str, b: str, c: str
    :return: SchemeEquationAnswer
    """
    answer = await controller_solution(equation)
    return answer
