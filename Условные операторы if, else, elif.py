first = input('Введите 1-ое число:  ')
second = input('Введите 2-ое число:  ')
third = input('Введите 3-ое число:  ')
value = [first, second, third]

'''Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0'''

if len(set(value)) == 1:
    print(f'Все числа равны между собой:  {3}')
elif len(set(value)) == 2:
    print(f'2 из 3 введённых чисел равны между собой:  {2}')
elif len(set(value)) == 3:
    print(f'Равных чисел среди 3-х нет:  {0}')
