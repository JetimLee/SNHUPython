# Here you can practice and get help on the exercise to find the smallest of 3 integers. Add code to do what the comments describe.

# For each of three numbers, prompt for it to be input and assign a variable to the integer value of what was input.

# Add conditional logic to calculate the smallest number. Your code should work even if two or all three of the numbers are equal.

# Print the smallest number.

number1 = int(input("input the first number"))
number2 = int(input("input the second number"))
number3 = int(input("input the third number"))

my_numbers = [number1,number2,number3]
print(min(my_numbers))

