#Author - Aldrich John P. Parantar
#Date - 10/15/2026
#Purpose - Evaluate and get a student's info based on their performance, classifying it into 5 keywords.

#STEP 1 - From the user, get two variables first number and second number, which will be used for calculations later.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#STEP 2 - Define functions that will calculate for the sum and the difference of the two numbers by order of first and then second number.

#FUNCTION A - Calculate the sum of the two numbers with number1 + number2 and then display to the user the result.
def calculate_sum():
    sum = number1 + number2
    print(f"Sum: {sum}")

#FUNCTION B - Calculate the difference of the two numbers with number1 - number2 and then display to the user the result
def calculate_difference():
    difference = number1 - number2
    print(f"Difference: {difference}")

#STEP 3 - Call the functions defined in the previous step to display their result.
calculate_sum()
calculate_difference()