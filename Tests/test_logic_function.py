from Logic.main import *


def test_random_integer_function()->None:
    if not isinstance(random_integer(), int):
        assert False, "Should return a random integer!"


def test_random_float_function()->None:
    if not isinstance(random_float(), float):
        assert False, "Should return a random floating number!"


def test_random_math_operation()->None:
    mathemtical_operations = ['+', '-', '*', '/', '%']
    if not random_math_operation() in mathemtical_operations:
        assert False, "Either not a Math Operation or not included!"


def test_evaluate_function()->None:
    assert evaluate("10 + 10") == 20, "evaluate function results in wronge result"
    assert evaluate("10 - 10") == 0, "evaluate function results in wronge result"
    assert evaluate("10 % 5") == 0 or evaluate("5 % 10") == 5, "evaluate function results in wronge result"
    assert evaluate("10 * 10") == 100, "evaluate function results in wronge result"
    assert evaluate("10 / 10") == 1, "evaluate function results in wronge result"
    assert evaluate("10 / 0") == "Undefined", "evaluate functionDivision by Zero was defined in this developer's script! lol"


if __name__ == '__main__':
    print("test_logic_functions.py from Tests!")
