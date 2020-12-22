def valid_float(number) -> bool:
    if isinstance(number, float):
        return True
    raise ValueError(f'The value {number} is not numeric')


def sum(number1: float, number2: float) -> float:
    if valid_float(number1) and valid_float(number2):
        return number1 + number2


def subtracion(number1: float, number2: float) -> float:
    if valid_float(number1) and valid_float(number2):
        return number1 - number2


def division(number1: float, number2: float) -> float:
    if number2 == 0:
        raise ValueError("It's not possible to divide by zero'")
    elif valid_float(number1) and valid_float(number2):
        return number1 / number2


def multiplication(number1: float, number2: float) -> float:
    if valid_float(number1) and valid_float(number2):
        return number1 * number2