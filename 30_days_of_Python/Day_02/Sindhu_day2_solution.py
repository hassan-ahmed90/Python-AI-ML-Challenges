#Q4. Create a program that prints the multiplication table of a given number.
"""number=int(input("enter a number: "))
print("--------------------------------")
print("multiplcaion table of ",number)
print("--------------------------------")
for i in range(1,11): # Loop from 1 to 10
    print(number,"x",i,"=",number*i)"""# Display the multiplication result

#Q5. Write a program to find the largest of three numbers. 
 #there are two types f solution 
#1 using logical operator"and" operator 
"""num1=int(input("enter number 1:"))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))

if num1>=num2 and num1>=num3:
    print(num1,"num1 is the largest.") 
elif num2>=num1 and num2>=num3:
        print(num2,"num2 is the largest.")
else:
        print(num3,"num3 is the largest.")"""

#2 using numpy 
"""import numpy as np

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))

numbers=np.array([num1,num2,num3]) # Store the numbers in a NumPy array
largest=np.max(numbers) # Find the largest number using NumPy
print("The largest number is",largest)"""

#Q6. Convert temperature from Celsius to Fahrenheit. 

celsius = float(input("Enter temperature in Celsius: "))
# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)