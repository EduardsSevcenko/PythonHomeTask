# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

from datetime import date

name="Eduards"
age=35
birthdate=date(1985, 9, 25)
print(name, age, birthdate, sep='\n')

a=int(input("enter 1st number from 0-100"))
b=int(input("enter 2nd number from 0-100"))
c=int(input("enter 3rd number from 0-100"))

d=str(input("enter your name"))
e=str(input("enter your surname"))
f=str(input("enter city of birth"))

print("1st number= " + str(a), "2nd number= " + str(b), "3rd number= " + str(c), "name= " + str(d), "surname= " + str(e), "city= " + str(e), sep='\n')

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import datetime
s=int(input("enter seconds= "))
res=datetime.timedelta(seconds=s)
print(res)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n=int(input("enter number "))
n2=str(n)*2
n3=str(n)*3
sum=n+int(n2)+int(n3)
print(sum)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

#A
print("Enter the Number :")
num=int(input())
Largest=0;
while (num > 0):
    reminder=num%10
    if Largest<reminder:
        Largest = reminder
    num =int(num / 10)
print("The Largest Digit is :", Largest)

#B
num=int(input("enter number "))
z=len(str(num))
y=0
for x in range(z):
    if(num%10>y):
        y=num%10
        num=num//10
    else:
       num=num//10
print("The Largest Digit is :", y)


# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

rev = int(input("enter revenue ="))
costs = int(input("enter costs ="))
profit = rev - costs
if profit < 0:
    print("Loss =", profit)
else:
    print("Profit =", profit)
margin = (profit/costs)*100
print(margin)

emp = int(input("enter employee number ="))
print(profit/emp)


'''6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км. '''

km = int(input("km in first day ="))
target = int(input("target km to reach ="))
i=1
while km <= target:
    i+=1
    km = km + km*0.1
print("target km reached =", round(km),"at the day of =", i)


