from app.models.calculation import Calculation
from app.schemas.calculation_schema import CalculationResponse


class CalculationService:
    @staticmethod
    def calculate(calculation):
        return calculation.execute()

    @staticmethod
    def perform_calculation(calc: Calculation) -> CalculationResponse:
        print(
            f"Received: operand1={calc.operand1}, operand2={calc.operand2}, operation={calc.operation}"
        )
        try:
            if calc.operation == "add":
                result = calc.operand1 + calc.operand2
            elif calc.operation == "subtract":
                result = calc.operand1 - calc.operand2
            elif calc.operation == "multiply":
                result = calc.operand1 * calc.operand2
            elif calc.operation == "divide":
                if calc.operand2 == 0:
                    raise ValueError("Division by zero")
                result = calc.operand1 / calc.operand2
            else:
                raise ValueError("Invalid operation")

            print(f"Result: {result}")
            return CalculationResponse(result=result)
        except Exception as e:
            print(f"Error: {e}")
            raise
