import unittest
import convert
#Task 2
def gather_numbers() -> list[float]:
    numbers = []
    while True:
        user_input = input("Please enter a number: ")
        if user_input.lower() == "done":
            break
        number = convert.str_to_float(user_input)
        if number is not None:
            numbers.append(number)

    print("Sum of numbers = ", sum(numbers))

if __name__ == "__main__":
        numbers = gather_numbers()
