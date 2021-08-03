# PI = 3.14
# def Circle_S():
#
#     r = int(input("Enter a radius of circle: "))
#
#     S = PI * (r**2)
#     print(S)
#
# def Circle_len():
#
#     d = int(input("Enter a diametr of circle: "))
#     C = PI * d
#     print(C)
#
# def interface():
#     print("Press 1. to chose calculation of Circle Squer.","\nPress 2. to chose calculation Circle lenght")
#     enter_point = int(input("Chose an option that you wont to calculate: "))
#     if enter_point == 1:
#         return Circle_S()
#     elif enter_point == 2:
#         return Circle_len()
#     else:
#         print("Opps! You entered somethig else")
#
# interface()

# number1 = int(input("enter number 1: "))
# number2 = int(input("enter number 2: "))
# print(number1 + number2, number1 - number2, number1 * number2, number1 / number2 )


#
# a = input("enter a number of 3 symbols: ")
# length = len(a)
# if length < 3:
#     print("Enter more symbols to 3")
# elif length > 3:
#     print("To much symbols,we need only 3")
# else:
#     b = list(a)
#     b.reverse()
#     print(b)
#     c = b.pop(0)
#     b.append(c)
#     print("".join(b))

# def cord(x,y):
#     if x >= 1 and 2 <= y <= 4:
#         return True
#
# print(cord(2,3))
#
# def fun(x,y):
#     z = x ** 2 - 2.5 * x * y + 5 * y ** 3
#     print(z)
#
# fun(3,4)

# def fun1(x,y,h):
#     S = 0.5 * (x + y) * h
#     print(int(S))
# fun1(3,4,6)

# a = input("enter: ")
# print(a[1],a[0],a[2], sep=",")

# def fun2(x,y):
#     if (x >= 2) and (y >= 1 or y <= -1.5):
#         print("True")
#     else:
#         print("False")
#
# fun2(3,2)

# import random
# n = 5
# m = 5
# a = []
#
# for i in range(n):
#     b = []
#     for j in range(m):
#         b.append(random.randint(-10,10))
#     a.append(b)
# print(a)
# c = []
# g = []
# for i in a:
#     d = []
#     f = []
#     for j in i:
#         if j < 0:
#             d.append(j)
#         else:
#             f.append(j)
#
#     c.append(d)
#     g.append(f)
# print(g)
# e = []
# for i in c:
#     if i:
#         e.append(max(i))
# print(e)
# max_val = -11
# index = -1
# for i in range(len(e)):
#     if e[i] > max_val:
#         max_val = e[i]
#         index = i
# min_val = 11
# index1 = -1
# x = []
# for i in g:
#     if i:
#         x.append(min(i))
# print(e)
# print(x)
#
# for i in range(len(x)):
#     if x[i] < 3:
#         min_val = g[i]
#         index1 = i
#
# temp = a[index]
# a[index] = a[index1]
# a[index1] = temp
# print(a)


# workers = {"Kuzin":{"name":"Bogdan","adres":"Kyiv"},
#            "Kubik":{"name":"Vasyl","adres":"Kharkiv"}}
# serch_name = input("Enter name")
# if serch_name in workers:
#     print(workers.get(serch_name) .get("adres"))

# countrys = {"Rodesia":{"Squer":123,"continent": "Africa"},
#             "Vietnam":{"Squer":435,"continent": "Asia"}}
# print(countrys.keys())
# for i  in countrys.keys():
#
#     if countrys[i] ["continent"] == "Africa":
#         print(countrys[i])

# import datetime
# students = {"Smith":{"name":"Olha","date_of_birth":datetime.datetime(2003,10,8)},
#             "Arkan":{"name":"Vasyl","date_of_birth":datetime.datetime(2003,9,13)},
#             "Seagul":{"name":"Petro","date_of_birth":datetime.datetime(2003,6,23)}}
# for key in students.keys():
#     date = (students.get(key).get("date_of_birth"))
#     curent_day = datetime.datetime.now()
#     if date.month == curent_day.month and date.day == curent_day.day:
#         print(f"Happy Birthday {key}")

# weather = {1:{"count": 15,"temperature":5},
#            2:{"count": 34,"temperature":0},
#            3:{"count": 28,"temperature":-1},
#            4:{"count": 22,"temperature":-5},
#            5:{"count": 13,"temperature":10}}
#
# rain = 0
# snow = 0
# for key in weather.keys():
#
#     if weather.get(key).get("temperature") >= 0:
#
#         rain += weather.get(key).get("count")
#     else:
#
#         snow += weather.get(key).get("count")
#
# print(rain,snow)

# import random
# cars = {}
# for i in range(30):
#     cars[i+1] = {"price": random.randint(3000,5000),
#                  "Hp": random.randint(70,150)}
# sum = 0
# more100 = 0
# for key in cars.keys():
#     if cars.get(key).get("Hp") >= 100:
#         sum += cars.get(key).get("price")
#         more100 += 1
#     else:
#         cars.get(key)["Hp"] += 20
# print(sum,more100)
# print(cars)

# finders = {"yahoo!": 2.09,"Google": 90.15,"Bing": 3.23,"Baidu":2.2}
# for key,value in finders.items():
#     print(key, ":", value)

