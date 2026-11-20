from helpers import banner
# -----------------------------------------
banner("Q4. Create a program that prints the multiplication table of a given number. ")
# -----------------------------------------
number = int(input("tell me any number and i'll tell you its multiplication table: "))
for num in range(1,11):
    count = number * num
    print(count)

# -----------------------------------------
banner("Q5. Write a program to find the largest of three numbers. ")
# -----------------------------------------
import numpy as np
numb = []
print("lemme see if i can find the greatest out of three number," \
    " go ahead and gimme any three: ")
for n in range(0,3):
    userNum = int(input())
    numb.append(userNum)
biggest = np.max(numb)
print(f"max number is {biggest}")

# -----------------------------------------
banner("Q6. Convert temperature from Celsius to Fahrenheit. ")
# -----------------------------------------
# the formula is f = (c*(9/5)+32)
c = float(input("what's the temperature in Celsius? "))
f = (c*(9/5)+32)
print(f"In Fahrenhiet that'll be {f}")
