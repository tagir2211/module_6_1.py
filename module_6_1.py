class animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        if self.food.edible:
            print(f'{self.name} съел {self.food.name}')
            self.fed = True
            print(f'{self.name} насытился')
        else:
            print(f'{self.name} не стал есть {self.food.name}')
            self.alive = False
            print(f'{self.name} умер потому что не стал есть {self.food.name}')
class plant:
    edible = False

    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Mammal(animal):
    def __init__(self, name):
        self.name = name
class Predator(animal):
    def __init__(self, name):
        self.name = name
class Flower(plant):
    def __init__(self, name):
        self.name = name


class Fruit(plant):
    edible = True
    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
