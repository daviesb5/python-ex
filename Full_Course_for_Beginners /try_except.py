# requires users to enter an integer

try:
    number = int(input("Enter a number: "))
    print(number)
# divided by zero
except ZeroDivisionError:
    print("Divided by zero")
# value error
except ValueError:
    print("Invalid input")
