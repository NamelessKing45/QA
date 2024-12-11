"""Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение),
recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию
sender = "university.help@gmail.com".
Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
Если же отправитель по умолчанию - university.help@gmail.com,
то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
Письмо отправлено с адреса <sender> на адрес <recipient>."
Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
За один вызов функции выводится только одно и перечисленных уведомлений!
Проверки перечислены по мере выполнения.
"""
def add(string):
    string += '/'
    if "@" in string and (".com" == string[-5:-1] or ".ru" == string[-4:-1] or
                             '.net' == string[-5:-1]):
        return True
    else:
        return False

def send_email(message: str, recipient: str, sender: str = "university.help@gmail.com"):
    if sender != "university.help@gmail.com" and add(sender) == True:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!")
    if sender == recipient and add(sender) == True:
        print("Нельзя отправить письмо самому себе!")
    else:
        if add(recipient) == True and True == add(sender) and sender != recipient:
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

send_email("1234564567", "123@rambler.ru")
print("\n")
send_email("1234564567", "123@rambler.ru", "333@rambler.ru")
print("\n")
send_email("1234564567", "123@rambler.ru", "123@rambler.ru")
