# nums = [1, 2, 5, 1, 8, 9, 15, 14, 2]
# sorted_nums = sorted(nums)   #sorted function sorts the list in ascending order
# print(sorted_nums)

# names = ['anish', 'Shreyas', 'tejas', 'Preshit', 'anish']
# sorted_names = sorted(names) 
# print(sorted_names)

#output = ['Preshit', 'Shreyas', 'anish', 'tejas'] and not ['anish', 'Preshit', 'Shreyas', 'tejas'] because of the case sensitivity

#Now we'll start with sets

# set(nums)               #this will give us a set of the list nums
# print(set(nums))      

# set(names)
# print(set(names))         #this will give us a set of the list names and will remove the duplicate values

# ninjas = {'ryu': 'black', 'yoshi': 'red', 'crystal': 'black'}
# print(ninjas.values())           #this will give us the values of the dictionary ninjas
# output = dict_values(['black', 'red', 'black']) 

# print(set(ninjas.values())) this will give us a set of the values of the dictionary ninjas
# output = {'black', 'red'}


def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f"There are {num} {belt} belts") 

ninja_belts = {}

while True:       # here while is true means it will run forever until we break it
    ninja_name = input("Enter a ninja name: ")
    ninja_belt = input("Enter a belt color: ")
    ninja_belts[ninja_name] = ninja_belt
    # here we are adding the key value pair to the dictionary 
    # ninja_belts is the dictionary and ninja_name is the key and ninja_belt is the value
    # print(ninja_belts) - Tutorial of whether the key value pair is added or not

    another = input("Add another? (y/n) ")
    if another == "y":
        continue
    elif another == "Ho":
        print("Ho Ho Ho")
    else:            
        break

belt_count(ninja_belts)

# Revision completed