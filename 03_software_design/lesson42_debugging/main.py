# try:
#     file = open("data.tex")
# except FileNotFoundError:
#     print("No file.")
# finally:
#     print("Program finished")

# age = -5

# if age < 0: 
#     raise ValueError("Age cannot be negative")

def safe_divide(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return "Cannot Divide by Zero"
    except TypeError:
        return "Invalid Input"

result = safe_divide(10, "2")
print(result)

import logging

logger = logging.getLogger(__name__)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Division by Zero.")
        return None
    except TypeError:
        logger.error("Invalid input type.")
        return None