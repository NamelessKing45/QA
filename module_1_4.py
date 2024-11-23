"""
1)Выведите строку my_string в верхнем регистре.
2)Выведите строку my_string в нижнем регистре.
3)Измените строку my_string, удалив все пробелы.
4)Выведите первый символ строки my_string.
5)Выведите последний символ строки my_string.
"""
my_string = str(input())

#1
print(my_string.upper())
#2
print(my_string.lower())
#3
print(my_string.replase(' ',''))
#4
print(my_string[0])
#5
print(my_string[-1])
