# Переделываем практическую:
#
# -Должен быть класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в файл
#
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты
import pickle
import json

class Notebook:

    file_path:str = 'products.json'
    file = None
    products:list = []

    def __init__(self):
        try:
            self.file = open(self.file_path, 'r+')
            try:
                self.products = json.load(self.file)
            except ValueError:
                self.products = []

        except FileNotFoundError:
            self.file = open(self.file_path, 'w+')

    def __del__(self):
        self.file.seek(0)
        json.dump(self.products, self.file)
        self.file.close()

    def write(self, product: str, price:int):
        self.products.append([product, price])

    def list(self):
        if len(self.products) == 0:
            raise Exception('У вас еще нет покупок')

        for product in self.products:
            print(f'{product[0]}, {product[1]}')


    def sum(self):
        if len(self.products) == 0:
            raise Exception('У вас еще нет покупок')

        print('Общая сумма: ', sum(item[1] for item in self.products))


    def max(self):
        if len(self.products) == 0:
            raise Exception('У вас еще нет покупок')

        max_priced = self.products[0]
        for product in self.products:
            if product[1] > max_priced[1]:
                max_priced = product
        print(f'{max_priced[0]} с ценой {max_priced[1]} стоит дороже остальных')

    def find(self, query: str):
        if len(self.products) == 0:
            raise Exception('У вас еще нет покупок')

        for product in self.products:
            if product[0].lower().find(query.lower()) != -1:
                print(f'Продукт: {product[0]}, цена: {product[1]}')




def menu():

    message = '''
    1) Создать запись
    2) Список все записей
    3) Общая сумма всех покупок
    4) Самая дорогая покупка
    5) Поиск по названию покупки
    9) Выход'''

    notebook = Notebook()

    print(message)
    while True:
        selected = input("Выберете вариант: ")
        try:
            if selected == '1':
                product = input('Укажите продукт: ')
                price = int(input('Введите цену: '))
                notebook.write(product, price)

            elif selected == '2':
                notebook.list()

            elif selected == '3':
                notebook.sum()

            elif selected == '4':
                notebook.max()

            elif selected == '5':
                query = input('Поиск:')
                notebook.find(query)

            elif selected == '9':
                return

            else:
                print('Не догнал. Выбирете правильный вариант:', message)

        except Exception as e:
            print(e)
menu()

