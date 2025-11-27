from random import randint, uniform, choice

mathemtical_operations = ['+', '-', '*', '/', '%']

def random_integer()->int:
    return randint(1, 10)


def random_float()->float:
    return round(uniform(1, 10), 2)


def random_math_operation()->str:
    return choice(mathemtical_operations)

# created 3 function for 3 levels of math expression
# Also to make it more readable
def easy()->str:
    return f"{random_integer()} {random_math_operation()} {random_integer()}"


def medium()->str:
    return f"({easy()}) {random_math_operation()} ({easy()})"


def difficult()->str:
    return f"{medium()}**2 {random_math_operation()} {medium()} {random_math_operation()} {medium()}"

def random_math_expression(difficulty:str)->str:
    if difficulty == "easy":
        return easy()
    elif difficulty == "medium":
        return medium()
    elif difficulty == "difficult":
        return difficult()
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
