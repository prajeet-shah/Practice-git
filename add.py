# add_numbers.py

def add_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b


def subtract_two_numbers(a, b):
    """
    Returns the difference of two numbers.
    """
    return a - b


def multiply_two_numbers(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b




def main():
    num1 = 5
    num2 = 10

    total = add_two_numbers(num1, num2)
    difference = subtract_two_numbers(num1, num2)
    product = multiply_two_numbers(num1, num2)

    

    print(f"Sum of {num1} and {num2}: {total}")
    print(f"Difference of {num1} and {num2}: {difference}")
    print(f"Product of {num1} and {num2}: {product}")

    print(f"Product of {num1} and {num2}: {product}")



if __name__ == "__main__":
    main()
