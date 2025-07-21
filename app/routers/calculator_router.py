from fastapi import APIRouter, HTTPException
from app.schemas.calculation_schema import CalculationRequest, CalculationResponse
from app.factory.calculation_factory import CalculationFactory
from app.services.calculation_service import CalculationService

router = APIRouter()


@router.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest):
    try:
        calculation = CalculationFactory.create_from_request(request)
        result = CalculationService.calculate(calculation)
        return CalculationResponse(
            operand1=request.operand1,
            operand2=request.operand2,
            operation=request.operation,
            result=result,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
