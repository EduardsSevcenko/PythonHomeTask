# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# p1 = int(input("p1="))
# p2 = int(input("p2="))

def div():
        p1 = int(input("p1="))
        p2 = int(input("p2="))
        try:
                return p1/p2
        except ZeroDivisionError:
                return "Not allowed to enter zero values"

"""      
        while p2 != 0 and p1 != 0:
                p1/p2
                return p1/p2
        else:
                print("Not allowed to enter zero values")
"""





print("p1/p2= ", div())
