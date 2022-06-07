from fastapi import APIRouter

from src.routers.equation.controller import controller_solution
from src.schemes.scheme_equation import SchemeEquation

router = APIRouter(
    prefix='/api/equation',
    tags=["equation"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def solution(equation: SchemeEquation):
    """

    :param equation:
    :return:
    """
    answer = await controller_solution(equation)
    return answer
