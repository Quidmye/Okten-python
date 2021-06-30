class Cinderella:

    count = 0

    def __init__(self, name:str, age:int, foot:int):
        self.name = name
        self.age = age
        self.foot = foot

        Cinderella.count += 1


class Prince:

    def __init__(self, name:str, age:int, slipper:int):
        self.name = name
        self.age = age
        self.slipper = slipper

    def find_cinderella_by_foot_size(self, cinderellas: list):
        for cinderella in cinderellas:
            if cinderella.foot == self.slipper:
                print(f'{cinderella.name} та саммая')
                return cinderella


cinderellas_list = [
    Cinderella('Даздрасмыгда', 13, 30),
    Cinderella('Даздраперма', 15, 29),
    Cinderella('Аврора', 12, 32),
    Cinderella('Беллатриса', 85, 36),
    Cinderella('Виолета', 19, 33),
    Cinderella('Абдула', 14, 28),
    Cinderella('Арианна', 17, 27),
    Cinderella('Мальберта', 19, 29),
    Cinderella('Азалия', 18, 30),
    Cinderella('Нимфадора', 17, 33)
]

prince = Prince('Лориерик', 20, 27);
prince.find_cinderella_by_foot_size(cinderellas=cinderellas_list)
print(Cinderella.count)


