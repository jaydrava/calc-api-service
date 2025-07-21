import pytest
from app.factory.calculation_factory import CalculationFactory
from app.models.calculation import Calculation, Operation
from app.schemas.calculation_schema import CalculationRequest
from pydantic import ValidationError


def test_calculation_add():
    calc = CalculationFactory.create_from_request(
        CalculationRequest(operand1=10, operand2=5, operation="add")
    )
    assert calc.execute() == 15


def test_calculation_subtract():
    calc = CalculationFactory.create_from_request(
        CalculationRequest(operand1=10, operand2=5, operation="subtract")
    )
    assert calc.execute() == 5


def test_calculation_multiply():
    calc = CalculationFactory.create_from_request(
        CalculationRequest(operand1=10, operand2=5, operation="multiply")
    )
    assert calc.execute() == 50


def test_calculation_divide():
    calc = CalculationFactory.create_from_request(
        CalculationRequest(operand1=10, operand2=5, operation="divide")
    )
    assert calc.execute() == 2


def test_divide_by_zero_raises():
    calc = CalculationFactory.create_from_request(
        CalculationRequest(operand1=10, operand2=0, operation="divide")
    )
    with pytest.raises(ValueError):
        calc.execute()


def test_invalid_operation_validation():
    with pytest.raises(ValidationError):
        CalculationRequest(operand1=10, operand2=5, operation="modulus")  # invalid op
