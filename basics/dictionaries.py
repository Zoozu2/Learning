# So dictionaries help us store key value pairs and we can access them using the key.

# ninja_belts = {"Tejas": "red", "shreyas": "blue"}
# print(ninja_belts)

# ninja_belts.values()
# print(ninja_belts.values())

# ninja_belts.keys()
# print(ninja_belts.keys())

# vals = list(ninja_belts.values())
# vals.count("red")
# print(vals.count("red"))

# ninja_belts["shreyas"] = "black"
# print(ninja_belts)["shreyas"]

def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f"I am {key} and I am a {val} belt")

ninja_belts = {}

while True:
    ninja_name = input("Enter a ninja name: ")
    ninja_belt = input("Enter a belt color: ")
    ninja_belts[ninja_name] = ninja_belt
    # here we are adding the key value pair to the dictionary 
    # ninja_belts is the dictionary and ninja_name is the key and ninja_belt is the value
    print(ninja_belts)
    another = input("Add another? (y/n) ")
    if another == "y":
        continue
    else:            
        break

ninja_intro(ninja_belts)
