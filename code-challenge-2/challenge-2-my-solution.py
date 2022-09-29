#smallest biggest integer game
#tackle advanced todos
from smtpd import DebuggingServer

usr_input = []
usr_inc_input = []

# new_variable = 'string'

# if new_variable == str:
#     print('its a string')
# elif (new_variable >= 0):
#     print('number')
# else:
#     print('something else')

#isinstance is best option to see if the value is a certain datatype
num = None
stringest = None
largest = 0
smallest = 0
clean = True
for i in range(20):
    new_input = input(
        "Put in a number up to 20 times or if done, type 'done'\n")
    for j in range(10):
        if str(j) in new_input:
            num = int(new_input)
            usr_input.append(num)
            break

    if (clean):
        if (num > largest):
            largest = num
        elif (num < smallest):
            smallest = num

    if (new_input.lower() == 'done' or i == 20):
        break
    else:
        stringest = new_input
        usr_inc_input.append(stringest)
        clean = False

print(usr_input)
print(usr_inc_input)
print(largest, smallest)