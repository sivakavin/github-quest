#creating add,subtract,multiplication,devision

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, operator, b):
    if operator not in OPERATIONS:
        raise ValueError(f"unknown operator: {operator}")
    return OPERATIONS[operator](a, b)


def main():
    while True:
        entry = input("Enter an expression (e.g. 3 + 2), or 'q' to quit: ").strip()
        if entry.lower() == "q":
            break
        try:
            a, operator, b = entry.split()
            print(calculate(float(a), operator, float(b)))
        except (ValueError, ZeroDivisionError) as error:
            print(f"error: {error}")


if __name__ == "__main__":
    main()
