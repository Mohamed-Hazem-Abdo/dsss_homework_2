import random
def rand_int(min, max):
    """
    Returns Random integer between given min and max values.
    """
    return random.randint(min, max)

def rand_operator():
    """
    Returns a string of Random operator between ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])

def problem_answer(num1, num2, op):
    """ takes two numbers as integers and an operator as a string
        Returns a string of the math problem and the answer as an integer.
      """
    problem = f"{num1} {op} {num2}"
    if op == '+': ans = num1 + num2
    elif op == '-': ans = num1 - num2
    else: ans = num1 * num2
    return problem, ans

def math_quiz():
    """ Math game that gives there random basic math questions,
        then takes the answer from the user and returns the score."""
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # getting random numbers and an operator to generate the question.
        num1 = rand_int(1, 10); num2 = rand_int(1, 5); op = rand_operator()
        flag = True      # a flag to indicate if the input is accepted or not
        problem, answer =problem_answer(num1, num2, op) # constructing the question and saving it and its answer.
        print(f"\nQuestion: {problem}")
        while flag:       #loop to indicate if the input is a valid number or not
            try:
                user_answer = int(input("Your answer: "))
                flag=False          # to break the loop in case of no value error
            except ValueError:
                print("the answer should be a valid number try again")
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
