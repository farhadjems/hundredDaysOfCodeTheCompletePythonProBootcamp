import os
import art


def add(n1, n2):
    return (n1 + n2)


def subtract(n1, n2):
    return (n1 - n2)


def multiplication(n1, n2):
    return (n1 * n2)


def division(n1, n2):
    return (n1 / n2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division,
}


def calculator():
    print(art.logo)
    user_continue = True
    num1 = float(input("What's the first number: "))

    while user_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation from above list: ")
        num2 = float(input("What's the next number: "))

        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        user_choice = input(
            f"type 'y' to continue calculating with {answer} or 'n' to exit: ")
        if user_choice == 'n':
            user_continue = False
            return
        else:
            num1 = answer
            os.system('clear')
            print(art.logo)


calculator()
