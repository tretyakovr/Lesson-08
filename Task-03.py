# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 8. Задание 3:
# Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать
# у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
# сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
#
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При
# вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить
# его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести
# текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class my_exception(Exception): pass

def get_value(name_value):
    input_value = input(f'\nВведите {name_value} (пустую строку для завершения ввода): ')

    return input_value


value_list = []

while True:
    input_value = get_value('элемент списка')
    if input_value == '':
        break

    try:
        input_value = int(input_value)
    except ValueError:
        print('Введено не числовое значение!')
    else:
        value_list.append(input_value)
        print('Введенное значение добавлено в список!')

print(value_list)