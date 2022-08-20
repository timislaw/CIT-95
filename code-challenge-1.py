import random



# first challenge due aug 21

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

# --------------------------------------------------- Separation -------------------------------------------------------


# Common error (one line) ...uncomment, run to see what happens, analyze and correct the syntax or logic error
some_decimal_number = float("1234.56")
# print(some_decimal_number)

# Common error (three lines) ...uncomment, run to see what happens, analyze and correct the syntax or logic error
some_decimal_number = float("1234.56")
annual_salary = some_decimal_number * 52
print(annual_salary)

# Print the new floating point number!
print(some_decimal_number)



# --------------------------------------------------- Separation -------------------------------------------------------

# Do the math!
# the "=" sign her is called the "assignment operator" and the following code statement is read as..
# "852.10 times twelve is assigned to my_math_number"
my_math_number = 852.10
print("I needed this number:", str(my_math_number * 12))

# Perform arithmetic on it to prove it's a number
my_new_num = some_decimal_number * 52

# Print out our new number (which looks like an annual salary!)
print(round(my_new_num, 2))
# added rounding to make it an annual salary


# Make our new number sound useful in a sentence.
# Remember, we must cast our number to a string in order to concatenate it.
# Do you feel like a programmer yet -- using all these coding words?
rounded_salary = round(my_new_num, 2)
print("\n\n The annual salary is $" + str(rounded_salary))

# Let's use an f-string to help with all these decimal numbers
# Take your time and learn f-string if you're doing anything with numbers or currency values.
# Review the reference on f-strings and you'll soon be friends with this new formatting tool
formatted_annual_salary = f'${my_new_num:,.2f}'
print("\n\nA better-looking salary figure: ", formatted_annual_salary, "\n\n")



# --------------------------------------------------- Separation -------------------------------------------------------

# challenge 2
# 2) Study the references and code up three examples from each reference -- your choice of topic (choose something
#    you always wanted to code.
x = abs(-5)
print(x)

max_addresses = bin(256)
print(max_addresses)

y = 'timothy'
print(y.capitalize())


# trimmed version of string
trim = '             this is the string\n before trimming'

print(trim.strip())

# line break split

print(trim.splitlines())

# all uppercase conversion

print(trim.upper())

# tuples are immutable
tuples = ('im', 'mute', 'able')

# list are mutable
list = ['mu', 'ta', 'ble']

# convert int to float

int = 10
print(float(int))

# --------------------------------------------------- Separation -------------------------------------------------------


def person_food_habits(name, food, habit):
    print(f"{name} eats {food} with his {habit}")

person_food_habits('tim', 'pizza', 'hand')

def my_salary(name, worked, pay):
    rounded_pay = float(pay)
    salary = worked * rounded_pay
    rounded_salary = str('{:.2f}'.format(salary))
    print(f"{name}'s annual salary working {worked} weeks at ${rounded_pay} per week is ${rounded_salary} USD per year. ")

my_salary('Tim', 52, 400.23)