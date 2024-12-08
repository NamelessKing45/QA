"""
Создайте модули fake_math и true_math.
Напишите функции divide в обоих методах. Разница между этими функциями - возвращаемое значение.
Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции divide из модулей fake_math и true_math, назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён, при помощи оператора as.
Запустите эти функции в модуле module_4_1, передав первым аргументом произвольное число отличное от 0, вторым аргументом - 0
Выведи результаты вызовов этих функций на экран(в консоль).
"""
from fake_math import divide as fake_divide
from true_math import divide as true_divide

fake_result = fake_divide(10, 0)
print("Результат работы fake_divide:", fake_result)
true_result = true_divide(10, 0)
print("Результат работы true_divide:", true_result)

