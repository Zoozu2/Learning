age = int(input("What is your age ? "))
natioinality = input("What is your n: ")

if age >= 18 and natioinality == "Indian":
    print("You can Vote")
elif natioinality != "Indian":
    print("smth")
else: 
    print("No you cannot vote")

