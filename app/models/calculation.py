from enum import Enum


class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"


class Calculation:
    def __init__(self, operand1: float, operand2: float, operation: Operation):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation

    def execute(self) -> float:
        if self.operation == Operation.add:
            return self.operand1 + self.operand2
        elif self.operation == Operation.subtract:
            return self.operand1 - self.operand2
        elif self.operation == Operation.multiply:
            return self.operand1 * self.operand2
        elif self.operation == Operation.divide:
            if self.operand2 == 0:
                raise ValueError("Division by zero")
            return self.operand1 / self.operand2
        else:
            raise ValueError("Invalid operation")
