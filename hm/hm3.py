# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:

    x = 0
    y = 0
    area = 0

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.area = x*y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return (self.y*2) + (self.x*2)


###############################################################################
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)

from abc import ABC, abstractmethod

class Trasnport(ABC):
    travel_time = 0

    def __lt__(self, other):
        return  self.travel_time > other.travel_time

    def __gt__(self, other):
        return  self.travel_time < other.travel_time

    def __sub__(self, other):
        return self.travel_time - other.travel_time

    def whats_better(self, other):
        better = self
        worse = other
        if(self < other):
            better, worse = worse, better

        print(f'{better.name} на {worse - better} годин швидший ніж {worse.name}')


class Plane(Trasnport):
    ticket_price = 0
    check_in_time = 0
    ticket_class = None
    name = 'Літак'

    def __init__(self, ticket_price: int, check_in_time: int, ticket_class: str, travel_time: int):
        self.ticket_price = ticket_price
        self.check_in_time = check_in_time
        self.ticket_class = ticket_class
        self.travel_time = travel_time

    def get_total_time(self):
        return self.check_in_time + self.travel_time

class Traine(Trasnport):
    ticket_price = 0
    ticket_type = None
    name = 'Поїзд'

    def __init__(self, ticket_price: int, ticket_type: str, travel_time: int):
        self.ticket_price = ticket_price
        self.ticket_type = ticket_type
        self.travel_time = travel_time

class Car(Trasnport):
    number_of_passengers = 0
    fuel_price = 0
    km = 0
    name = 'Машина'

    def __init__(self, number_of_passengers: int, fuel_price: int, km: int, travel_time: int):
        self.number_of_passengers = number_of_passengers
        self.fuel_price = fuel_price
        self.km = km
        self.travel_time = travel_time

    def get_total_price(self):
        return self.km*self.fuel_price

car = Car(4, 5, 100, 50)
plane = Plane(45, 5, 'перший', 40)
car.whats_better(plane)



######################################################################

# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

emptyList = []

class Letter:

    __count = 0

    def __init__(self, text):
        Letter.__count += 1

        self.__text = text

    def get_count(cls):
        return cls.__count

    def put_text_to_list(self):
        global emptyList
        emptyList.append(self.__text)

let = Letter('dsadas')
let2 = Letter('dsadaddsdsadas')
let3 = Letter('dsaddsadsaas')
let.put_text_to_list()
let2.put_text_to_list()
let3.put_text_to_list()
print(emptyList, let.get_count())
