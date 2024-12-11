"""
Создайте класс Car. Добавьте обязательные атрибуты класса: модель,
год выпуска, объем двигателя, цена, пробег, количество колес = 4.

Создайте 1 экземпляр класса

Создать класс наследник - Грузовик. Который, наследует все атрибуты класса, но количество колес = 8.

Создать 1 экземпляр класса Наследника

Добавить метод, который возвращает информацию по объекту (как в учебном видео метод description)

Вы должны выполнить данное задание самостоятельно, используя те знания и материалы,
которые вы получили в курсе и прислать решение на проверку.
"""

class Car:
    def __init__(self, model, year_manufacture, engine_capacity, price, mileage):
        self.model = model;self.year_manufacture = year_manufacture;self.engine_capacity = engine_capacity
        self.price = price;self.mileage = mileage;self.number_wheels = 4

    def description(self):
        return (f"1) Модель: {self.model};\n2) Год выпуска: {self.year_manufacture};\n"
                f"3) Объем двигателя: {self.engine_capacity};\n4) Цена: {self.price};\n"
                f"5) Пробег: {self.mileage};\n6) Количество колес: {self.number_wheels};.")


car = Car(model='Toyota Camry', year_manufacture=2020, engine_capacity=2.5, price=30000, mileage=15000)
print(f'\nХарактеристики легкового автомобиля:\n{car.description()}')

class Truck(Car):
    def __init__(self, model, year_manufacture, engine_capacity, price, mileage):
        super().__init__(model, year_manufacture, engine_capacity, price, mileage)
        self.number_wheels = 8

truck = Truck(model='Volvo FH', year_manufacture=2022, engine_capacity=12.8, price=120000, mileage=5000)
print(f'\nХарактеристики грузовика:\n{truck.description()}')
