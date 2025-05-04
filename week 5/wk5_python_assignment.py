# ACTIVITY ONE

class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level
    
    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I’m level {self.level}!")

    def attack(self):
        print(f"{self.name} attacks using {self.power} at level {self.level}!")


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, level, flying_speed):
        super().__init__(name, power, level)
        self.flying_speed = flying_speed

    def attack(self):
        print(f"{self.name} swoops in at {self.flying_speed} km/h and attacks using {self.power}!")

    def fly(self):
        print(f"{self.name} is flying at {self.flying_speed} km/h!")


hero1 = Superhero("ThunderMan", "Electric Shock", 5)
hero2 = FlyingSuperhero("SkyWing", "Wind Blade", 7, 300)

hero1.introduce()
hero1.attack()

print()

hero2.introduce()
hero2.attack()
hero2.fly()

# ACTIVITY TWO



class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky.")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water.")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the trail.")


vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()