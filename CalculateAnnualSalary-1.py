# CalculateAnnualSalary.py
# dH 8/8/22
#
# CIT-95 Fall 2022 Module 01 Code Challenge
#
# 1) Work through the code below and complete any Common Error exercises (uncomment, correct, run, repeat).
# 2) Study the references and code up three examples from each reference -- your choice of topic (choose something
#    you always wanted to code.
# 3) Write a program with the following:
#       classes and methods: None
#       control structures: Sequence
#       data structures: Strings (arguably... a string is a Python data structure!)
#       error handling: None
#       functions: At least two user-defined functions. One with 3 parameters corresponding to the 3 user-input values
#           and another that will accept a string and find and return the first dollar amount in the string. You will
#           also use at least 3 of the 67 bulit-in Python functions -- print(), float(), str()
#       input: User input for:
#           name, number of weeks worked in a year, weekly pay
#       output: A string echoing the input values and the calculated annual salary properly
#            formatted in US Standard English e.g. "Katrina's annual salary working 52 weeks at $852.10 per
#            week is $10,225.20 USD per year." (Annual means yearly, but it is good to say things twice when
#            dealing with money.
#       processing: Calculate annual pay (weekly pay * 12)
#
# References:
# https://www.w3schools.com/python/python_ref_functions.asp
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_datatypes.asp
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
#
print("\n\n\n\n")
print("Welcome to CIT-95 Fall 2022 Module 01 Code Challenge!")

# print two blank lines
print()
print()

# print six lines
print("\n\n\n\n\n\n")

# Create three variables with hard-coded values.
name = "Dmitriy"
weeks = "22 weeks"
weekly_pay = "$1234.56 per week"

# Create a long string with concatenation.
# Notice how age was converted to string because only strings can be concatenated!
long_string = name + " worked " + weeks + " for " + weekly_pay + "!"

# Output the concatenated, long string containing hard-coded values.
print("\n\n", long_string, "\n\n")

# How can we calculate an annual salary when we have a number inside a string?
# We must extract the number from the string (we use the Python string method find() for this) and
# then convert that string to a float (a decimal number) data type. We can't perform arithmetic on a string,
# so we must convert a string to a number. in this case, we want to convert to a floating point number so we
# can use decimal numbers.

# Convert a string to a float.
# The variable named some_decimal_number is assigned the newly "casted" float value

some_decimal_number = float("1234.56")

# Common error (one line) ...uncomment, run to see what happens, analyze and correct the syntax or logic error
#   some_decimal_number = float("$1234.56")

# Common error (three lines) ...uncomment, run to see what happens, analyze and correct the syntax or logic error
#   some_decimal_number = ("1234.56")
#   annual_salary = some_decimal_number * 52
#   print(annual_salary)

# Print the new floating point number!
print(some_decimal_number)

# Do the math!
# the "=" sign her is called the "assignment operator" and the following code statement is read as..
# "852.10 times twelve is assigned to my_math_number"
my_math_number = 852.10
print("I needed this number:", str(my_math_number * 12))

# Perform arithmetic on it to prove it's a number
my_new_num = some_decimal_number * 52

# Print out our new number (which looks like an annual salary!)
print(my_new_num)

# Make our new number sound useful in a sentence.
# Remember, we must cast our number to a string in order to concatenate it.
# Do you feel like a programmer yet -- using all these coding words?
print("\n\n The annual salary is $" + str(my_new_num))

# Let's use an f-string to help with all these decimal numbers
# Take your time and learn f-string if you're doing anything with numbers or currency values.
# Review the reference on f-strings and you'll soon be friends with this new formatting tool
formatted_annual_salary = f'${my_new_num:,.2f}'
print("\n\nA better-looking salary figure: ", formatted_annual_salary, "\n\n")


# Let's create a function so we can reuse our code whenever we need to!
# Our function is named find_number (notice we use snake_style -- lowercase words with underscores between them)
# and has one parameter that it uses to get input. Our new function will process the string passed to it by finding
# the number hidden in the string using the find() method.
# reference for find(): https://www.w3schools.com/python/ref_string_find.asp note that find(0 work like index()
# but index throws an exception if its argument is not found, while find() returns a -1 in this case

def find_number_hiding_in_str(the_str_num):
    # Create a variable to hold the result
    the_number_result = 0.0
    the_index = the_str_num.index("$")
    return the_index

# put our formatted salary in a sentence
pay_statement = "Dmitriy made " + str(formatted_annual_salary) + " last year."
print(pay_statement)

# Call our new function in a print statement and see where our salary starts
# Strings are numbered starting a 0 and counting up by one with each letter
# e.g. for "the amount is $12,987" t is index 0, h is index 1, e is index 2, ...
# We just created the string: "Dmitriy made $64,197.12 last year" -- count characters starting with zero for
# the "D" in Dmitriy and you will be at 13 when you find the $ sign!
print("   the $ in our figure is at index: ", str(find_number_hiding_in_str(pay_statement)))

# Now that we know where our $ sign is, we know that our number starts at this position (index) plus one. We will
# use substring to get our number out of the string.
# Here's the reference: https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/

# Now that we know the staring index of our number, let's find the end of our number, the space after the dollar sign.
# Although we know the starting position of our search for the space is 13, we will use our

index_of_space_after_money = pay_statement.find(" ", find_number_hiding_in_str(pay_statement))
print(index_of_space_after_money)

# Now that you have all the code you need for this challenge... code up the two functions mentioned at the
# top of this challenge. Good luck!
