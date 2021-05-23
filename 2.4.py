# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

input_text = input("Enter text: ")
input_words = input_text.split(' ')

print(input_words)

for word in input_words:
    index = input_words.index(word)
    print(index+1, word[:10])
