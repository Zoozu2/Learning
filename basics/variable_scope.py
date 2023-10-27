# my_name = 'Shreyas'   # Global variable as we have defined it at the highest level of the program

# def print_name():
#     # my_name = 'Shreyas'   # Local variable as we have defined it inside a function
#     # Also if we change the value of my_name inside the function, it will not affect the value of my_name outside the function
#     print('My name is', my_name)

# print_name()

# print ('You an also call me', my_name)

# Lets make changes in the local variable and see if it affects the global variable

my_name = 'Shrey'

def print_name():
    global my_name
    my_name = 'Rohan'
    print('My name is', my_name)

print_name()
print ('You an also call me', my_name)