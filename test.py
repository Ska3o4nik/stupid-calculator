# Дебильный калькулятор версия 1.0

from colorama import init
from colorama import Fore, Back, Style
init()


do = input("Выберите Действие: \n +, -, *, /. \n")

first = float(input("Введите первое число: "))

second = float(input("Введите второе число: "))

if do == '+':
    answer = first + second
    print(Back.GREEN)
    print("Ответ: " + str(answer))
elif do == '-': 
    answer = first - second
    print(Back.GREEN)
    print("Ответ: " + str(answer))
elif do == '*':
    answer = first * second
    print(Back.GREEN)
    print("Ответ: " + str(answer))
elif do == '/':
    answer = first / second
    print(Back.GREEN)
    print("Ответ: " + str(answer))
else:
    print(Back.RED)
    print('Вы не выбрали действие!')

input()