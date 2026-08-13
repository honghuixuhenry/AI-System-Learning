# number = int(input("Enter a number: "))

# print(number)

# try:
#     number = int("abd")
# except ValueError:
#     print("Please input a number.")
# finally:
#     print("finished.")

# age = -10
# if age < 0:
#     raise ValueError("Age cannot be negative.")

# try:
#     number = int("abd")
# except ValueError:
#     print("input error")

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("division by zero error")

# age = -5
# if age<0:
#     raise ValueError("Negative age is not allowed.")

try:
    print("Start")
    print(10/0)
except ZeroDivisionError:
    print("Catch")
finally:
    print("Finally")