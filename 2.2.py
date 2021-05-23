# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

list = []

n = int(input("Enter number of items in list : "))

for i in range(0, n):

    list.append(int(input("Enter number :"))) # adding the items

print(list)
for index in range(0, len(list)-1, 2):
    list[index], list[index+1] = list[index+1], list[index]
print(list)

# result_list = []
# #
# for element in list[::2]:
#     index = list.index(element)
#     if index+1 == len(list):
#         result_list.append(element)
#     else:
#         first_element, second_element = list[index], list[index+1]
#         result_list.extend([second_element, second_element])
# print(result_list)