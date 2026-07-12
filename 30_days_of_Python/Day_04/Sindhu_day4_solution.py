# Q10. Program to find the sum of first N natural numbers
n=int(input("enter a number"))
total = 0
# adding numbers from 1 to n
for i in range (1,n+1):
    total += i
print("sum=",total)


# Q11. Number Guessing Game

import random
# selects a random number between 1 and 10
secret_number = random.randint(1 ,10)
guess = int(input("guess a number between 1 to 10: "))
if guess==secret_number:
    print("conguraulation! you gased it correctly")
else:
    print("wrong guess.The number was",secret_number)
    

# Q12. Program to print all prime numbers between 1 and 100
print ("prime numbers between 1 and 100 are ")
# Checking each number from 2 to 100
for num in range(2 ,101):
    is_prime = True

    # Checking whether the number is divisible by any smaller number
    for i in range (2,num):
        if num % i==0:
            is_prime=False
            break

     # Printing the number if it is prime   
    if is_prime:
        print(num, end=" ")

