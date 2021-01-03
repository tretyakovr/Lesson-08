# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 8. Задание 2:
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте
# его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой

# Я не до конца уверен в правильности решения. Задачу выполнил, ошибки обрабатываются, программа не
# завершается ошибкой, но фактически я нигде не использовал my_exception
class my_exception(Exception):
    pass

def get_value(name_value):
    input_value = input(f'\nВведите {name_value} (пустую строку для завершения ввода): ')

    return input_value


while True:
    divisible = get_value('делимое')
    if divisible == '':
        break

    divisor = get_value('делитель')
    if divisor == '':
        break

    try:
        division = int(divisible) / int(divisor)
    except ZeroDivisionError:
        print('Ошибка: делитель не должен быть равен нулю!')
    except ValueError:
        print('Ошибка преобразования введенного значения!')
    else:
        print(f'Частное равно {division}')