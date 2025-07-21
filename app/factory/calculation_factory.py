from app.schemas.calculation_schema import CalculationRequest
from app.models.calculation import Calculation


class CalculationFactory:
    @staticmethod
    def create_from_request(request: CalculationRequest) -> Calculation:
        return Calculation(
            operand1=request.operand1,
            operand2=request.operand2,
            operation=request.operation,
        )
