Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(a, b)
...     return a + b  # SyntaxError (Missing :)
... 
... def subtract(a, b):
...     return a - b
... 
... def multiply(a, b):
...     return x * b  # NameError (x is not defined)
... 
... def divide(a, b):
...     return a / b  # ZeroDivisionError (No handling for division by zero)
... 
... print("Simple Calculator")
... num1 = input("Enter first number: ")
... num2 = input("Enter second number: ")
... operation = input("Choose operation (+, -, *, /): ")
... 
... if operation == "+":
...     print("Result:", add(num1, num2))  # TypeError (num1 and num2 are strings)
... elif operation == "-":
...     print("Result:", subtract(num1, num2))
... elif operation == "*":
...     print("Result:", multiply(num1, num2))
... elif operation == "/":
...     print("Result:", divide(num1, num2))
... else:
...     print("Invalid operation")
