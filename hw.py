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

# class BankAccount ():
#     def __init__(self, ownerName, initialBalance, accountNumber):
#         self.__ownerName = ownerName
#         self.__balance = initialBalance
#         self.__accountNumber = accountNumber

#     def getOwnerName(self):
#         return self.__ownerName
                
#     def getBalance(self):
#         return self.__balance

#     def getAccountNumber(self):
#         return self.__accountNumber   

#     def setOwnerName(self, name):
#         if name is not None and name != '':
#             self.__ownerName = name
#         else:
#             print("Пустое или неправильное имя")

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Счет пополнен на {amount}")
#         else:
#             print("Ошибка: Сумма пополнения должна быть положительной.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 print(f"Со счета снято {amount}.")
#             else:
#                 print("Мало средств")

#     def displayAccountInfo(self):
#         print(f"Информация о счете:")
#         print(f"Владелец: {self.__ownerName}")
#         print(f"Номер счета: {self.__accountNumber}")
#         print(f"Баланс: {self.__balance}")

# account = BankAccount("Чумиков Игорь", 1000, "456456465")
# account.displayAccountInfo() 
# account.deposit(3300)   
# account.withdraw(2000)   
# account.withdraw(1000)  
# account.deposit(-100)   
# account.displayAccountInfo()


# ----------------------------hw 22.07

# Задание №1. Множества
# Даны два списка:
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [5, 6, 7, 8, 9, 10, 11]
# Преобразуйте их в множества.
# Найдите:
# ● Общие элементы (intersection)
# ● Элементы, которые есть только в a (difference)
# ● Все уникальные элементы из обоих списков (union)
# ● Удалите элемент 10 из второго множества.

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [5, 6, 7, 8, 9, 10, 11]
# a = set(a)
# b = set(b)
# c = a.intersection(b)
# d = a.difference(b)
# e = a.union(b)
# b.discard(10)

# Задание №2. List comprehension
# Дан список чисел:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ● Создайте новый список, содержащий только чётные числа из
# numbers.
# ● Создайте список квадратов чисел из numbers.
# ● Создайте список, в котором все числа из numbers заменены на строку
# "чётное" или "нечётное" в зависимости от их значения.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [i for i in numbers if i % 2 == 0]
# square_numbers = [i ** 2 for i in numbers]
# even_or_not = ['чет' if i % 2 == 0 else 'нечет' for i in numbers]
# print(even_or_not)

# Задание №3 и №4 Упаковка и распаковка
# Напишите функцию print_kwargs, которая принимает произвольное
# количество именованных аргументов и выводит их в формате
# ключ=значение.
# Пример вызова:
# print_args(1, 2, 3,"hello")

# def print_kwargs(**kwargs):
#     for key in kwargs:
#         print(f'{key} = {kwargs[key]}')
# print_kwargs(name = 'Igor', age = '34', work = 'hr')


# --------------------------------- hw 24/07

# import pandas as pd

# data = {'name': ['Игорь', 'Ажелика', 'Андрей', 'Полина1', 'Полина2', 'Ян', 'Дима', 'Тимур'],
#         'age': [34, 24, 15, 18, 19, 93, 38, 29],
#         'city': ['Сочи', 'Сочи', 'Ростов', 'Адлер', 'Анадырь', 'Архипоосиповка','Нью-йорк', 'Архипоосиповка']}

# df = pd.DataFrame(data)

# print(df.describe()) #Статистика по числовым столбцам
# print(df['age'].value_counts().sort_index())  # частотность возрастов
# print(df['city'].value_counts()) # статистика по городам
# print(df[df['age'] > 30]) #Фильтрация по возрасту
# print(df.nsmallest(1, 'age'))
# print(df.nlargest(1, 'age'))
# print(df.groupby('city')['age'].mean())

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

class CarDealership:
    def __init__(self, name):
        self.name = name
        self.available_cars = []  
        self.sold_cars = []       
        self.expenses = 0         
        self.income = 0           
        self.profit = 0          
        
    def add_car(self, model, sale_price, purchase_price):
        car = {
            'model': model,
            'sale_price': sale_price,
            'purchase_price': purchase_price,
            'status': 'available'
        }
        self.available_cars.append(car)
        self.expenses += purchase_price
        self._calculate_profit()
        print(f"Добавлена машина: {model} (Цена продажи: {sale_price}, Закупочная: {purchase_price})")
    
    def sell_car(self, model):
        car_found = False
        for car in self.available_cars:
            if car['model'] == model and car['status'] == 'available':
                car['status'] = 'sold'
                self.sold_cars.append(car)
                self.income += car['sale_price']
                self._calculate_profit()
                print(f"Продана машина: {model} за {car['sale_price']}")
                car_found = True
                break
        
        if not car_found:
            print(f"Машина {model} не найдена или уже продана")
    
    def add_expense(self, amount, description):
        if amount < 0:
            print("Ошибка: сумма расходов не может быть отрицательной")
            return
        self.expenses += amount
        self._calculate_profit()
        print(f"Добавлены расходы: {description} на сумму {amount}")
    
    def _calculate_profit(self):
        self.profit = self.income - self.expenses
    
    def search_car(self, model):
        found_cars = [car for car in self.available_cars if car['model'] == model and car['status'] == 'available']
        if not found_cars:
            print(f"Машина {model} не найдена в наличии")
            return None
        return found_cars
    
    def get_stats(self):
        stats = {
            'available_count': len([car for car in self.available_cars if car['status'] == 'available']),
            'sold_count': len(self.sold_cars),
            'total_income': self.income,
            'total_expenses': self.expenses,
            'profit': self.profit
        }
        return stats
    
    def print_stats(self):
        stats = self.get_stats()
        print(f"\n=== Статистика автосалона '{self.name}' ===")
        print(f"Машин в наличии: {stats['available_count']}")
        print(f"Машин продано: {stats['sold_count']}")
        print(f"Общий доход: {stats['total_income']}")
        print(f"Общие расходы: {stats['total_expenses']}")
        print(f"Прибыль: {stats['profit']}\n")
    
    def print_available_cars(self):
        print("\n=== Доступные машины ===")
        available = [car for car in self.available_cars if car['status'] == 'available']
        if not available:
            print("Нет доступных машин")
            return
        
        for car in available:
            print(f"{car['model']} - Цена продажи: {car['sale_price']}")


if __name__ == "__main__":
    dealership = CarDealership("СочиАвто")
    
    dealership.add_car("Лада", 25000, 20000)
    dealership.add_car("Нива", 23000, 18000)
    dealership.add_car("Запорожец", 55000, 45000)
    dealership.add_car("Ваз", 26000, 21000)  
    
    dealership.add_expense(5000, "Аренда")
    dealership.add_expense(3000, "Зарплата")
    

    dealership.sell_car("Лада")
    dealership.sell_car("Ваз")  
    
    print("\nПоиск машины:")
    found = dealership.search_car("Запорожец")
    if found:
        print(f"Найдена: {found[0]['model']} за {found[0]['sale_price']}")
    
    dealership.print_stats()
    dealership.print_available_cars()