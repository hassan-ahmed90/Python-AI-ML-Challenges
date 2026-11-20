from helpers import banner
# -----------------------------------------
banner("Q7. Write a program to calculate the factorial of a number using a loop.")
# -----------------------------------------
num = int(input("\nEnter a number to caclculate the factorial: "))
factorial=1                                       #bcz we multiply it so can't make it 0
for num in reversed(range(1 , num+1)):            #num+1 bcz for loop stops b4 the biggest num, tere was no need for reversed but added to make it 3*2*1 not 1*2*3 like we study
    factorial *= num
print(factorial, "\n")

# -----------------------------------------
banner("Q8. Create a program to count the number of vowels in a string.")
# -----------------------------------------
String = input("\nEnter any sentnce to count it's vowels: \n")
count = 0
for vowel in String.strip().lower():
    if vowel in "aueoi":
        count += 1
print("Vowels count in your phrase: ", count, "\n")

# -----------------------------------------
banner("Q9. Write a Python script to reverse a given string.")
# -----------------------------------------
text = input("Enter any text you want to reverse: ")
revText=""
for rev in reversed(text.strip()):
    revText += rev
print("Reversed text is: ", revText)