# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list=[]

my_list.extend(['a', 'b', 'c'])
my_list.append('k')
my_list.append(1)
my_list.append([2, 4])
my_list.insert(3, 'w')
print(my_list)

for ele in my_list:
    print("List element: ", ele, "type: ", type(ele))
