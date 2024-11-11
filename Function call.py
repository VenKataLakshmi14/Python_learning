def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if b != 0:
        result = a / b
    else:
        result = "Error! Division by zero."
    return result

def greet(name):
    return f"Hello, {name}!"

def main():
    x = 10
    y = 5
    print(f"The sum of {x} and {y} is: {add(x, y)}")
    print(f"The difference when {x} is subtracted from {y} is: {subtract(x, y)}")
    print(f"The product of {x} and {y} is: {multiply(x, y)}")
    print(f"The quotient when {x} is divided by {y} is: {divide(x, y)}")
    user_name = "Alice"
    print(greet(user_name))

if __name__ == "__main__":
    main()

    #hai

