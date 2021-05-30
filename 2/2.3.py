# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
a = int(input("Enter number of month: "))
my_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
my_dict2 = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
key_list = list(my_dict2.keys())
val_list = list(my_dict2.values())
lst = list(val_list)
# position = val_list.index(a)
# print(type(val_list), lst)
# print(key_list[position])

for k,v in my_dict2.items():
    if v == a:
        print(k)
        break
else:
    print("")
print(k)
# seasons_dict=seasons_dict.fromkeys([12, 1, 2], "Winter")
#
#
# print(seasons_dict.get(number_of_month, ''))
