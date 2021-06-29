#прога, що виводить кількість кожного символа з введеної строки,
stri = input('Вводи: ')
for s in set(stri):
    print(f"'{s}' ->", stri.count(s))


# 1)  есть лист:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# создать новый лист и записать в него 'GT' если элемент в numbers больше 4 и 'LT' если элемент меньше или равен 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
lst = ['LT' if n <= 4 else 'GT' for n in numbers]

# 2) есть два листа:
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
#
# записать в лист тюплы (x,y) если x+y == 0

list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
lst2 = [(s, j) for j in list2 for s in list1 if j+s == 0]