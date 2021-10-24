#Задача «Минимум из двух чисел»
#Даны два целых числа. Выведите значение наименьшего из них.
first_number=int(input())
second_number=int(input())
if first_number>second_number:
    print(second_number)
else:
    print(first_number)