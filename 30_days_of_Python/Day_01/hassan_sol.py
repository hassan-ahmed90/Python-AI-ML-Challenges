# Q1. Write a Python program to swap two variables. 
a=1
b=2
print("Before Swaping: a=", a, "b=", b)
c=a
a=b
b=c
print("After Swaping: a=", a, "b=", b)

# Q2. Take user input and display it back to the user. 

name= input("Enter your name:")
print(f"Your name is {name}")

# Q3. Write a program to check if a number is even or odd.
number = int(input("Enter the number to check if it is even or Odd"))

if number % 2 ==0 :
	print(f" {number} is Even")
else:
	print(f"{number} is Odd ")