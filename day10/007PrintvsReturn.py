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

num1 = float(input("What's the first number: "))

for symbol in operations:
    print(symbol)

operation = input("Pick an operation from above list: ")
num2 = float(input("What's the next number: "))
answer = operations[operation](num1, num2)
print(f"{num1} {operation} {num2} = {answer}")

operation = input("Pick an operation from above list: ")
num3 = float(input("What's the next number: "))

new_answer = operations[operation](answer, num3)
print(f"{answer} {operation} {num3} = {answer}")
