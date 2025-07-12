# hw 26.06


# Задание №4.
# Вывести чётные числа от 1 до 20
# Используя цикл, выведите все чётные числа в диапазоне от 1 до 20.

# for evenNumber in range(2,21,2):
#     print(evenNumber)

# Задание №5
# Вывести квадраты чисел от 1 до 10
# Напишите программу, которая выводит квадраты всех чисел от 1 до 10.

# for Number in range(1,11):
#    Number *=Number
#    print(Number)

# Задание №6
# Сумма чётных чисел от 1 до 100
# Найдите и выведите сумму всех чётных чисел от 1 до 100.

# sumEven = 0
# for evenNumber in range(2,101,2):
#     sumEven += evenNumber
# print(sumEven)

# Задание №7 Фукнции
# Проверка чётности
# Напишите функцию is_even(num), которая возвращает True, если число
# чётное, и False — если нет

# def isEven(num):
#     return num % 2 == 0
# print(isEven(10))    

# Задание №8. Функции
# Максимум из трёх чисел
# Создайте функцию max_of_three(a, b, c), которая возвращает наибольшее
# из трёх чисел

# def max_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# print(max_of_three(432,1,45))

# или через max

# def max_of_three(a,b,c):
#     return max(a,b,c)
# print(max_of_three(40,20,30))

# Задание №9. Фукнции
# Длина строки
# Напишите функцию str_length(s), которая возвращает длину строки без
# использования len().

# def str_length(s):
#     sum = 0
#     for word in s:  
#         sum +=1
#     return sum
# print(str_length('Приветики'))
    

# ---------------------hw 01.07

# def details(birth,educ,work):
#     return 'Chumikov Igor Valerievich'


# Задание №1. Декоратор
# Написать оригинальную функцию, которая представляет ваше ФИО.
# Создать декоратор, который будет представлять вашу дату рождения.
# Создать декоратор, который будет представлять ваше образование.
# Создать декоратор который будет представлять вашу сферу деятельност


# def data(born):
#     def wrapper():
#         print(born)
#     return wrapper

# def educ(hedu):
#     def wrapper():
#         print(hedu)
#     return wrapper

# def work(hr):
#     def wrapper():
#         print(hr)
#     return wrapper

# def about(data,educ,work):
#     print('Chumikov Igor Valeriech')
#     data()
#     educ()
#     work()

# data = data('18.10.1990')
# work = work('hr')
# educ = educ('hu hr')

# about(data,educ,work)

# Задание №2 Лямбда Выражения
# Написать функции лямбда выражения которые будут менять значение в
# переменной.

# sum = lambda sum: sum+sum
# mult = lambda mult: mult * mult

# print(mult(5))

# Задание №3. Мини программа “Преобразование типов”
# Написать программу которая будет преобразовывать типы данных.
# Реализовать возможность выбора пользователем тип данных через
# терминал

# value = int(input("введите число"))
# choice = input('Преобразовать в(1-2):\n1 простое \n2 с плавающей точкой')

# if choice == '1':
#     value == int(value)
#     print(value)
# else:
#     value = float(value)
#     print(value)



# ---------------Hw 03.07

# Задание №2.
# Напишите класс который представляет фабрику и производит продукты
# питания. Отличает готовые и не готовые продукты.

# class fabric:
#     def __init__(self):
#         self.cooked = []
#         self.raw = []
#     def addCooked (self, name):
#         self.cooked.append(name)
#     def addRaw (self,name):
#         self.raw.append(name)

# foodFactory = fabric()


# foodFactory.addCooked('мяско')
# foodFactory.addCooked('питса')
# foodFactory.addCooked('курочка')
# foodFactory.addRaw('рыба')
# foodFactory.addRaw('паста')
# foodFactory.addRaw('овощи')

# print('готовые продукты:',foodFactory.cooked)
# print('сырые продукты:',foodFactory.raw)


# ----------------------hw 08.07

# Задание №2 Техническое задание для разработки программы учета
# автосалона
# Нужна программа для управления автосалоном. Она должна помогать
# следить за машинами, которые есть в наличии, учитывать проданные,
# считать доходы и расходы.
# Основное:
# ● В системе должны храниться данные о машинах (модель, цена
# продажи, закупочная цена).
# ● При продаже машина должна уходить из списка доступных и
# добавляться в проданные.
# ● Нужно учитывать все траты: закупка машин, зарплаты, аренда и
# прочее.
# ● Программа должна автоматически считать прибыль (доходы минус
# расходы).
# Дополнительно:
# Хорошо бы видеть статистику: сколько машин в наличии, сколько продано,
# общий доход, расходы и прибыль.
# Если можно, добавить поиск по модели, чтобы быстро находить машину в
# списке.

class carShowroom:
    def __init__(self):
        self.carInShow = []
        self.soldCar = []
        self.expenses = []
        self.income = 0

    def addCar(self,model,sellingPrice,purchasePrice):
        self.model = model
        self.sellingPrice = sellingPrice
        self.purchasePrice = purchasePrice
        self.carInShow.append(model,sellingPrice,purchasePrice)

show = carShowroom()
show.addCar("Лада Веста",100000500000,1000000)
print(show)