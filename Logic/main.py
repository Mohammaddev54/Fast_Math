from random import randint, uniform, choice

mathemtical_operations = ['+', '-', '*', '/', '%']

def random_integer()->int:
    return randint(0, 9)


def random_float()->float:
    return round(uniform(0, 9), 2)


def random_math_operation()->str:
    return choice(mathemtical_operations)


def random_math_expression()->str:
    return f"{random_integer()} {random_math_operation()} {random_integer()}"


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
