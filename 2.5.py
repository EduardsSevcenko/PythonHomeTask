# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [9, 7, 5, 3, 3, 1]
rating_copy = rating.copy()

input_rating=int(input(" Enter new element in rating: "))
if input_rating > rating[0]:
    rating_copy.insert(0, new_rating)
elif input_rating < rating[-1]:
    rating_copy.append(input_rating)
else:
    for rate in rating:
        if input_rating == rate:
            rating_index = rating.index(rate)
            rating_count = rating.count(rate)
            rang_index = rating_index + rating_count
            rating_copy.insert(rang_index, input_rating)
            break
        elif input_rating > rate:
            rating_copy.insert(rating.index(rate), input_rating)
            break
        else:
            continue
print(rating_copy)


