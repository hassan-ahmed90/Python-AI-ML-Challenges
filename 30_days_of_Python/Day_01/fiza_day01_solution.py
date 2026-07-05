#Q1. Write a Python program to swap two variables. 
a , b = 5 , 10
print(f"Before swap: a = {a} , b = {b}")
temp = a
a = b
b = temp
print(f"After swap: a = {a}, b = {b}" )

#Q2. Take user input and display it back to the user. 
name = input("Enter your name:" )
age = int(input("Enter you age: "))
print("Name", name)
print("Age", age)
#Q3. Write a program to check if a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
  print(num,"is an Even number")
else:
  print(num,"is an odd number")