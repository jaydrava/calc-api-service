from pydantic import BaseModel, Field, field_validator
from enum import Enum


class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"


class CalculationRequest(BaseModel):
    operand1: float = Field(..., description="First operand")
    operand2: float = Field(..., description="Second operand")
    operation: Operation

    @field_validator("operand2")
    def check_division_by_zero(cls, v, info):
        if info.data.get("operation") == Operation.divide and v == 0:
            raise ValueError("Division by zero is not allowed")
        return v


class CalculationResponse(BaseModel):
    operand1: float
    operand2: float
    operation: Operation
    result: float
