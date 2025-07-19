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

# class carShowroom:
#     def __init__(self):
#         self.carInShow = []
#         self.soldCar = []
#         self.expenses = []
#         self.income = 0

#     def addCar(self,model,sellingPrice,purchasePrice):
#         self.model = model
#         self.sellingPrice = sellingPrice
#         self.purchasePrice = purchasePrice
#         self.carInShow.append(model,sellingPrice,purchasePrice)

# show = carShowroom()
# show.addCar("Лада Веста",100000500000,1000000)
# print(show)


# ------------------17.07


# Задача: "Защищённый калькулятор"
# Напишите калькулятор, который запрашивает у пользователя два числа и
# операцию (+, -, *, /), а затем выводит результат.
# Обработайте возможные исключения:
# ● Деление на ноль.
# ● Ввод нечисловых значений.
# ● Неизвестная операция.

# while True:
#         numA = input('Введите целое первое число')
#         numB = input('Введите целое второе число')
#         try:
#                 numA = int(numA)
#                 numB = int(numB)
#                 break
#         except ValueError:
#                 print('Будем пробовать до конца жизни, пока не введем целые числа')
# while True:
#         oper = input('Введите операнд (+, -, *, /)')
#         if oper == '+' or oper == '-' or oper == '*' or oper == "/":
#             break
#         print('С операндами также, будем пробовать до конца жизни')

# if oper == '+':
#         print(numA + numB)
# elif oper == '-':
#         print(numA - numB)
# elif oper == "*":
#         print(numA * numB)
# elif oper == "/":
#         try:
#             print(numA / numB)
#         except ZeroDivisionError:
#             print('Только дурачки делят на 0')
                        
        
# Задача: "Анализатор списка"
# Напишите функцию, которая принимает список чисел и возвращает:
# 1. Минимальное и максимальное значение.
# 2. Среднее арифметическое.
# 3. Список без дубликатов.

# def process_number(numbers):
#     min_num = min(numbers)
#     max_num = max(numbers)
#     arith_mean = sum(numbers) / len(numbers)
#     unique_num = set(numbers)

#     return {
#         'min': min_num,
#         'max': max_num,
#         'mean': arith_mean,
#         'unique': unique_num
#     }
    
# numbers = [1,124,3,5,6,7,1,3,5,73,745,56,2,0,-23,-21,-112,23,43]
# print(process_number(numbers))
  
# Задача “Магазин”
# Есть кортеж с продуктами:
# products = ("яблоки", "молоко","хлеб","сыр")
# Задания:
# ● Вывести первый и последний продукт из списка.
# ● Проверить, есть ли "молоко" в списке.
# ● Посчитать, сколько всего продуктов в списке.

# products = ("яблоки", "молоко", "хлеб", "сыр")
# print(products[0])
# print(products[-1])
# milk = 'молоко'
# if milk in products:
#     print('Молоко есть в списке')
# print(len(products))


# ------------hw 19.07

# Создать класс BankAccount, представляющий банковский счет, с
# соблюдением правил инкапсуляции.
# Требования:
# Поля класса (должны быть приватными):
# ownerName (String) — имя владельца счета.
# balance (double) — текущий баланс.
# accountNumber (String) — номер счета.
# Конструктор:
# Должен принимать параметры: ownerName, initialBalance,
# accountNumber.
# Инициализирует все поля.
# Геттеры (методы доступа):
# getOwnerName() — возвращает имя владельца.
# getBalance() — возвращает текущий баланс.
# getAccountNumber() — возвращает номер счета.
# Сеттеры (методы изменения с проверками):
# setOwnerName(String name) — изменяет имя владельца (не должно
# быть null или пустым).
# (Для balance и accountNumber сеттеры не нужны, так как их
# изменение происходит через специальные методы).
# Методы для операций со счетом:
# deposit(double amount) — пополняет счет на указанную сумму (сумма
# должна быть положительной).
# withdraw(double amount) — снимает деньги со счета (сумма должна
# быть положительной и не превышать баланс).
# В обоих методах должны быть проверки, а в случае ошибки — вывод
# сообщения.
# Дополнительный метод:
# displayAccountInfo() — выводит информацию о счете (владелец, номер,
# баланс).

class BankAccount ():
    def __init__(self, ownerName, initialBalance, accountNumber):
        self.__ownerName = ownerName
        self.__balance = initialBalance
        self.__accountNumber = accountNumber

    def getOwnerName(self):
        return self.__ownerName
                
    def getBalance(self):
        return self.__balance

    def getAccountNumber(self):
        return self.__accountNumber   

    def setOwnerName(self, name):
        if name is not None and name != '':
            self.__ownerName = name
        else:
            print("Пустое или неправильное имя")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Счет пополнен на {amount}")
        else:
            print("Ошибка: Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Со счета снято {amount}.")
            else:
                print("Мало средств")

    def displayAccountInfo(self):
        print(f"Информация о счете:")
        print(f"Владелец: {self.__ownerName}")
        print(f"Номер счета: {self.__accountNumber}")
        print(f"Баланс: {self.__balance}")

account = BankAccount("Чумиков Игорь", 1000, "456456465")
account.displayAccountInfo() 
account.deposit(3300)   
account.withdraw(2000)   
account.withdraw(1000)  
account.deposit(-100)   
account.displayAccountInfo()