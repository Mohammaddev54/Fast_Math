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
