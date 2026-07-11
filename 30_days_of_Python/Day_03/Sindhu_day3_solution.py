# Q7. Program to calculate the factorial of a number using a loop
num = int(input("enter the number ")) #input number from the user
factorial =1 
# Multiplying numbers from 1 up to the entered number
for i in range (1,num+1):
    factorial = factorial*i

    print("factorial=",factorial) # Displaying the final factorial value


# Q8. Program to count the number of vowels in a string

text = input("Enter a sentence: ")#input string from the user
count = 0

for ch in text: # Checking each character one by one
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels in sentence:", count) #Printing the total number of vowels


# Q9. Program to reverse a given string
text = input("enter a string:")
reverse_text = ""
for ch in text:# Adding each character at the beginning of the new string
    reverse_text = ch+reverse_text

print("reversed string:",reverse_text)
