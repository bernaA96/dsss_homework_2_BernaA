import random


def random_int(min_value, max_value):
    """
    A random integer is expected to be generated within the specified range.
    """
    return random.randint(min_value, max_value)


def random_operator():
    """
    Choosing a random mathematical operator.
    """
    return random.choice(['+', '-', '*'])


def calculate(n1, n2, operator):
    """
    A mathematical operation is performed between two numbers.
    """
    p = f"{n1} {operator} {n2}"

    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2

    return p, answer


def math_quiz():
    """
    Main function to start the math quiz game.
    The function generates a series of math problems, checks the user's answers and displays the final score.
    """

    result = 0  # This variable is used to keep track of the user's score
    number_of_questions = 5  # Fixed number of questions for the quiz because it was not integer value

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_questions):
        n1 = random_int(1, 10);
        n2 = random_int(1, 6);  # Generating a random integer between 1 and 6 (5.5 replaced with 6)
        operator = random_operator()

        PROBLEM, ANSWER = calculate(n1, n2, operator)
        print(f"\nQuestion: {PROBLEM}")

        try:  # Getting user's answer and handling invalid inputs
            useranswer = int(input('Your answer: '))

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                result += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

        except ValueError:  # Handling cases where user does not enter a valid integer
            print('Invalid input. Please enter an integer!')
            continue  # Skipping to the next question if input is invalid

    print(f"\nGame over! Your score is: {result}/{number_of_questions}")  # Displaying the final score


if __name__ == "__main__":
    math_quiz()
