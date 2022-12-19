#!/usr/bin/env python3
# import "ipdb"

def admin_login(username, password):
    # your code here
    return 'Access granted' if username.lower() == 'admin' and password == '12345' else 'Access denied'
    pass

def hows_the_weather(temp):
    # your code here
    if temp < 40:
        return("It's brisk out there!")
    elif temp >= 40 and temp < 65:
        return("It's a little chilly out there!")
    elif temp > 85:
        return("It's too dang hot out there!")
    else:
        return("It's perfect out there!")
    pass

def fizzbuzz(num):
    # your code here
    if not num % 5 and not num % 3:
        return "FizzBuzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    else: return num
    pass

def calculator(operation, num1, num2):
    # your code here
    try:
        if operation == "+":
            number = num1 + num2
        elif operation == "-":
            number = num1 - num2
        elif operation == "*":
            number = num1 * num2
        elif operation == '/':
            number = num1 / num2
        return number
    except:
        print("Invalid operation!")
        return None 
    pass
