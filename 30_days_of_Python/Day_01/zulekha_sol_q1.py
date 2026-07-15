# Q1. Write a Python program to swap two variables

a , b = 5 , 10
print(f"before swapping: {a , b}")
a , b = b , a
print(f"after swapping: {a , b}")

# Q2. Take user input and display it back to the user. 

name = input("what's your name?")
print(f"Hi, nice to meet you {name}")

#  Q3. Write a program to check if a number 

num = int(input("give me any number and i'll tell you if it's odd or even: "))
if num%2==0:
    print(f'{num} is even')
else:
 print(f'{num} is odd')
