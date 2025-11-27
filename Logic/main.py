from .mathematical_functions import *

correct = 0
wrong = []


def log_wrong_answers_in_text_file():
    global wrong
    with open("wrong_answers.txt", "w") as file:
        for i in wrong[::-1]:
            file.write(i)


def difficulty_level_choice()->str:
    while True:
        # Changed the wording from hard -> difficult
        print("Difficulty Levels: (Easy), (Medium), (Difficult)")
        levels = ["easy", "medium", "difficult"]
        difficulty_level = input("Difficulty: ").strip().lower()
        if difficulty_level not in levels:
            continue
        return difficulty_level


def main()->None:
    global correct, wrong
    
    number_of_math_expression = round(float(input("how many math expression do you want enter a number: ")))
    level_choice = difficulty_level_choice()
    while number_of_math_expression > 0:
        expression = random_math_expression(difficulty=level_choice)
    
        print(expression, end=" = ")
    
        user_entered_number = input("")
        # Bug If user enters empty value expression will be called again
        # Thus showing new expression
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
