#Q4. Create a program that prints the multiplication table of a given number.
#  # Prompt the user to input a number
num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}:")

for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")

#Q5. Write a program to find the largest of three numbers. 
# Prompt user to input three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Compare numbers using logical operators
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Output the result
print(f"The largest number is: {largest}")

#Q6. Convert temperature from Celsius to Fahrenheit. 
# Accept temperature input from the user in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the result formatted to 2 decimal places
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
