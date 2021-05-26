# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_list():
    import numbers
    string = input(" :")
    test = list(string.split(" "))
    total = 0
    for element in test:
        if isinstance(element, int) or element.isdigit():
            total += int(element)
    print(total)

sum_list()
#

# continue_calc= True
# result_sum=0
# while continue_calc:
#     string=input(" :")
#     current_sum, continue_calc=sum_list()
#     result_sum += current_sum
#     print(result_sum)
# print(result_sum)
