def divide_numbers():
    try:

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))


        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")

    except ValueError:
        print("Error: Please enter a valid integer number.")

    finally:
        print("Execution complete.")

divide_numbers()
