name = "Shreyas"
age = 24
nums = [1, 2, 3, 4, 5]

# print(type(name))
# print(type(age))
# print(type(nums))

# Class is a blueprint for creating new objects

#print(name.upper())   #here name is an object of the class string and upper is a method of the class string
#output = SHREYAS

class Planet:
    def __init__(self):  #here we used __init__ method to initialize the object
        self.name = 'Earth'
        self.radius = 200000
        self.gravity = 9.8
        self.system = 'Solar System'
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

world = Planet()
print(f'Name is {world.name}')
print(f'Radius is {world.radius}')
print(f'Gravity is {world.gravity}')
print(f'System is {world.system}')
print(world.orbit())

# Name is Earth
