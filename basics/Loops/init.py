class Planet:
    def __init__(self, name, radius, gravity, system):  #here we used __init__ method to initialize the object and its attributes
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

world = Planet('Earth', 200000, 5.5, 'Solar System')
print(f'Name is {world.name}')
print(f'Radius is {world.radius}')
print(f'Gravity is {world.gravity}')
print(f'System is {world.system}')

nabo = Planet('Naboo', 300000, 8, 'Naboo System')

print(f'Name is {nabo.name}')
print(f'Radius is {nabo.radius}')
print(f'Gravity is {nabo.gravity}')
print(f'System is {nabo.system}')

print(nabo.orbit()) 

