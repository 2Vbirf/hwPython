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
    