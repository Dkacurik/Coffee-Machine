class House():
    def __init__(self, construction):
        self.construction = construction
        self.elevator = True

# object of the class House
new_house = House("building")

print(new_house.construction, new_house.elevator)
