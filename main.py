from Logic.main import *


def main()->None:
    correct = 0
    rounds = round(float(input("Enter a number: ")))
    total_rounds = rounds
    while rounds > 0:
        expression = random_math_expression()
        print(expression, end=" = ")
        user_result = input("")
        if check_user_input(expression=expression, user_input=user_result):
            correct += 1
        #else:
        #    print("Wrong!")
        #    print(f"Correct answer is: {evaluate(expression=expression)}")
        print("--------------------")
        rounds -= 1
    else:
        print(f"{correct} out of {total_rounds} is correct!")


if __name__ == "__main__":
    main()
