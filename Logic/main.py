<<<<<<< HEAD
from mathematical_functions import *

correct = 0
wrong = []


def log_wrong_answers_in_text_file():
    global wrong
    with open("wrong_answers.txt", "w") as file:
        for i in wrong[::-1]:
            file.write(i)


def main()->None:
    global correct, wrong
    
    number_of_math_expression = round(float(input("how many math expression do you want enter a number: ")))
    
    while number_of_math_expression > 0:
    
        expression = random_math_expression()
    
        print(expression, end=" = ")
    
        user_entered_number = input("")
    
        if not user_entered_number != "":
            print("Empty!")
            print("--------------------")
            continue
    
        if check_user_input(expression=expression, user_input=user_entered_number):
            correct += 1
        else:
            wrong.append(f"Question (#{number_of_math_expression}), expression: {expression}, User: {user_entered_number}, Correct answer: {evaluate(expression=expression)}\n")
    
        print("--------------------")
        number_of_math_expression -= 1
    
    print(f"{correct} out of {correct + len(wrong)} is correct!")
    
    if len(wrong) > 0:
        log_wrong_answers_in_text_file()



if __name__ == "__main__":
    main()
=======
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
>>>>>>> origin/main
