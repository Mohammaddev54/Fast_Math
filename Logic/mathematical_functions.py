from random import randint, uniform, choice

mathemtical_operations = ['+', '-', '*', '/', '%']

def random_integer()->int:
    return randint(1, 10)


def random_float()->float:
    return round(uniform(1, 10), 2)


def random_math_operation()->str:
    return choice(mathemtical_operations)


def random_math_expression(difficulty:str)->str:
    if difficulty == "easy":
        return f"{random_integer()} {random_math_operation()} {random_integer()}"
    elif difficulty == "medium":
        return f"({random_integer()} {random_math_operation()} {random_integer()}) {random_math_operation}\
            ({random_integer()} {random_math_operation()} {random_integer()})"
    elif difficulty == "hard":
        return f"{random_integer()}**2 * {random_integer()} + {random_integer()}"
    else:
        return f"0"


def evaluate(expression:str):
    try:
        return round(eval(expression), 2)
    except ZeroDivisionError:
        return "Undefined"


def validate_user_input(user_input):
    try:
        return round(float(user_input), 2)
    except ValueError as error:
        print(error)
        return 0

def check_user_input(expression, user_input):
    if evaluate(expression=expression) != validate_user_input(user_input=user_input):
        return False
    return True


if __name__ == '__main__':
    print("main.py from Logic Directory!")
