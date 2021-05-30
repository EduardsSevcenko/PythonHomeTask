# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
import random

def sumMax2():
    a=[]
    n = int(input ("Range numbers from 0:"))
    N = int(input ("Enter count of numbers:"))
    for i in range(0,n):
        num = random.randint(1, N)
        a.append((num))
        a.sort(reverse=True)
        b = sum(a[:2])
    print("List :", a,'\n',"Sum of largest 2 numbers in list = ", b)

sumMax2()



