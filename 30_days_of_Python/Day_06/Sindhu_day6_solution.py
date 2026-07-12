# Q16. Calculator app using if-else.

# Taking two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Taking the operator from the user
operator = input("Enter an operator (+, -, *, /). Type your choice: ")


if operator == "+": # Performing the selected operation
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not possible.")

else:
    print("Invalid operator.")


# Q17. Program to find the square root of a number.

import math

num = float(input("Enter a number: "))

# Finding the square root
result = math.sqrt(num)


print("Square root =", result)# print the result


# Q18. Program to check whether a number is prime or not.

num = int(input("Enter a number: "))

if num < 2:  # Numbers less than 2 are not prime
    print(num, "is not a prime number.")

else:
    is_prime = True

    
    for i in range(2, num):  # Checking if the number is divisible by any number from 2 to num-1
        if num % i == 0:
            is_prime = False
            break

    # Displaying the result
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")


# Q19. Program to display the cube of numbers up to an integer.
#take input from user 
n = int(input("Enter an integer: "))

# Finding and displaying cubes from 1 to n
for i in range(1, n + 1):
    cube = i ** 3
print("Cube of", i, "is", cube)