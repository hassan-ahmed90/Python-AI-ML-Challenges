# Q13. Program to calculate the sum of digits of a number.

# Taking a number from the user
num = int(input("Enter a number: "))
total = 0

# Adding each digit to the total
while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

# Displaying the sum of digits
print("Sum of digits =", total)

# Q14. Program to find the second largest number in a list.

numbers = [12, 45, 8, 67, 23, 90, 34]# Creating a list of numbers

numbers.sort()# Sorting the list in ascending order

print("Second largest number is:",numbers[-2])

# Q15. Program to count the number of digits in an integer.

num = int (input("Enetr a numbers: "))#take input from user 
count =0

while num>0:# Counting the digits one by one
    num=num//10
    count +=1
print("you type",count,"number of digits =")# Displaying the total number of digits