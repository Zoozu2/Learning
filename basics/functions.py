# Basically functions means a block of code that performs a specific task.
# Functions are used to avoid repetition of code.
 
# Syntax of a function
# def function_name():
#     code to be executed

# def greet():
#     print("Hello World")

# greet()

# output = Hello World - This will print the function and also the output of the function

# def greet(name,time):
#     print(f'Good {time} {name}, hope you are well.')

# name = input('Enter your name: ')
# time = input('Enter the time of the day: ')

# Remember the order of the arguments should be same as the order of the parameters in the function
# greet(name,time)


def area(radius):
    return (3.142 * radius * radius)

def vol(area,length):
    print(area*length)

radius = int(input('Enter your choice of radius:'))
length = int(input('Enter your choice of length:'))

# area_radius = area(radius) - Rather than doing this 
# we can directly call the function in the vol function
    
vol(area(radius),length)

