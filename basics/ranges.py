# For Loops revision
# data = [1, 2, 3, 4, 5]
# for num in data:
#     print(num)

# for n in range(5):
#     print(n)

# for n in range (4,10):
#     print(n)

# 1st parameter - Start value, 2nd parameter - End value, 3rd parameter - Difference
# for n in range (0, 20, 4):
#     print(n)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

for n in range(len(burgers) -1, -1, -1):
    print(n, burgers[n])

# So today we have learnt about ranges and how to use them in for loops
# We have also learnt about the len() function and how to use it to get the length of a list
# We have also learnt how to use the range function to iterate over a list backwards
# We have also learnt how to use the range function to iterate over a list with a start and end value and a step