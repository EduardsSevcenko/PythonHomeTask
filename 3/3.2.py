# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

""" 1 """
# def profile(**kwargs):
#     return kwargs
#
# print(profile(name="Eduards", surname="Shevchenko", birthdate="25.09.1985", city="Riga", email="eduards.sevcenko@gmail.com", tel="+371 2999999"))

""" 2 """
# dict={'name': 'Eduards', 'surname': 'Shevchenko', 'birthdate': '25.09.1985', 'city': 'Riga', 'email': 'eduards.sevcenko@gmail.com', 'tel': '+371 2999999'}
# for key, value in dict.items():
#     print(key, ' : ', value)

""" 3 """
def profile(d):
    d={}

f=dict()
f.update(name=input("name:"), surname=input("surname:"), birthdate=input("birthdate:"), city=input("city:"), email=input("email:"), telephone=input("telephone:"))
print(f)


""" 4 """
# record = int(input("Enter the number of record need to add :"))
#
# data={}
#
# for i in range(0, record):
#     Name = input("Enter the name :").split()
#     Surname = input("Enter the {} Surname :".format(Name))
#     Birthdate = input("Enter the {} Birthdate :".format(Name))
#     City = input("Enter the {} City :".format(Name))
#     email = input("Enter {} email :".format(Name))
#     phone = input("Enter the {} phone :".format(Name)).split()
#     Name_key = Name[0]
#     Surname_key = Surname[0]
#     Birthdate_key = Birthdate[0]
#     City_key = City[0]
#     email_key = email[0]
#     phone_key = phone[0]
#     data = {"Name:": Name,"Surname:": Surname,"Birthdate:": Birthdate,"City:": City,"email:": email,"phone:": phone}   """ (A) """
#     for key, value in stud_data.items():
#         print(key, ' : ', value)


"""data[Name_key] = {Surname_key,Birthdate_key, City_key,email_key,phone_key}
print(data)""" """ (B) """


