# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
strings = input('Вводи: ')
lt = [i for i in strings if i.isdigit()]
print(', '.join(lt))

# написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані
nStr = input('Вводи 2:')
lst = list()
tmp = ''
i = 0
for s in nStr:
    if s.isdigit():
        tmp += s
    if len(nStr) == i + 1 or not s.isdigit():
        if len(tmp) > 0:
            lst.append(tmp)
            tmp = ''
    i += 1
print(', '.join(lst))


#записать каждый символ в лист поменяв его на верхний регистр
greeting = 'Hello, world'
lis = [s.upper() for s in greeting]


#с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
list3 = [i**2 for i in range(0, 50) if i%2 != 0 or i == 0]

# - створити функцію яка виводить ліст
def printList(myList):
    print(myList)

#створити функцію яка приймає три числа та виводить та повертає найменьше.
def minOfThree(one, two, three):
    print(min([one, two, three]))
    return min([one, two, three])


#- створити функцію яка приймає три числа та виводить та повертає найбільше.
def maxOfThree(one, two, three):
    print(max([one, two, three]))
    return max([one, two, three])


#- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def returnMinPrintMax(*args):
    print(max(args))
    return min(args)

#- створити функцію яка повертає найбільше число з ліста
def maxOfList(lst):
    return max(lst)

#- створити функцію яка повертає найменьше число з ліста
def minOfList(lst):
    return min(lst)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sumOfList(lst):
    return sum(lst)

#- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def averageOfList(lst):
    return sum(lst) / len(lst)


# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

def lineToSpace(func):
    result = func()
    return result.replace('_', ' ')

@lineToSpace
def pr():
    return 'Hello_boss_!!!'

print(pr)



