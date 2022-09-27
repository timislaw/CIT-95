#code challenge 2
#basic 1
import numpy as np
#basic 2
#two vars datatype none
largest = None
smallest = None

#create array to hold input
user_int_array = []

for i in range(20):
    user_int_array.append(999)

# print(user_int_array)

#create loop tracker
num_of_loops = 0

#create array to hold strings
user_str_array = []

for i in range(5):
    user_str_array.append(f"0000000000000{i+1}")

# print(user_str_array)

#basic 3

clean_input = True

#basic 4

print(
    'BignSmall Numbers Game -- Enter up to 20 integers and enter done \n to stop the game. Type a string to to test exceptions'
)

num = input("Enter a number (\"done\" to stop): \n")

largest = num
smallest = num

#print(largest, smallest)

num_of_loops = 0
num_of_user_strs = 0

#write loop
while (True):
    clean_input = True

    # if (num == 'done'):
    #     print('done')
    #     break
    # elif (int(num) <= 20):
    #     print(num)
    #     break
    # else:
    #     print('invalid input')
    #     break
    #kept erroring

    if (num == 'done' or num_of_loops == 20):
        break
    try:
        (isinstance(int(num), int))
        #returns true instead of the type
    except:
        print('invalid input')
        clean_input = False
        #means we put in an invalid input, so we set the clean_input flag to false to signify wrong input
        user_str_array[num_of_user_strs] = num
        #the [0] index will equal the input, then adding 1 to increase for next index
        num_of_user_strs += 1

    if (clean_input):
        num = int(num)
        #turn num into int
        # print(type(num))
        if (num > int(largest)):
            largest = num
        if (num < int(smallest)):
            smallest = num
        user_int_array[num_of_loops] = num

    num_of_loops += 1
    num = input("Enter a new number (\"done\" to stop): \n")

print('largest num is', largest)
print('smallest num is', smallest)

print("\nUser input was: ")
for item in user_int_array:
    print(item)
print("\n\n")
print("Invalid user input was: ")
for item in user_str_array:
    print(item)
print("\n\n")

# TODO: Advanced 01) Output the user-input arrays without the unused elements i.e. 999, 0000000000004.
# TODO: Advanced 02) Use a Python list instead of two arrays
# TODO: Advanced 03) Create this program without needing the try/except block
# TODO: Advanced 04) Use persistent storage (File I/O) to store user data -- who played the game and when, what was
#                    their big and small number
