"""
Напишите проект "Калькулятор".
Инструкции к заданию:
Напишите скрипт "калькулятор", который будет принимать от пользователя на вход:
1-е число
арифметический знак, один из: +, -, *, /
2-е число
производить сложение, вычитание, умножение или деление, в зависимости от введенного знака
А так же предусмотрите проверку на то, что на ноль делить нельзя. И другие виды некорректно введенных данных.
Данное задание Вам необходимо выполнить самостоятельно и стараться не пользоваться сторонними источниками
"""
try:
    value1 = int(input("Введите первое число  "))
    sign = input("Введите функцию   ")
    value2 = int(input('Введите второе число  '))
    normal_sign = "/*+-"
    if sign in normal_sign:
        if sign == normal_sign[0]:print(f'{value2} {sign} {value1} =',value1 / value2)
        elif sign == normal_sign[1]:print(f'{value2} {sign} {value1} =',value1 * value2)
        elif sign == normal_sign[2]:print(f'{value2} {sign} {value1} =',value1 + value2)
        elif sign == normal_sign[3]:print(f'{value2} {sign} {value1} =',value1 - value2)
    else:print("Введены некорректные данные")
except ValueError:print("Введены некорректные данные")
except ZeroDivisionError:print("Делить на ноль нельзя!")




