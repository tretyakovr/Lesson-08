# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 8. Задание 4:
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для
# приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

import shop

dev1 = shop.projector('LCD', '800x600', 10000)
dev1.model_name = 'Проектор Philips NeoPix Easy+ серебристый'
dev1.serial_num = '111111'
dev1.country = 'China'
dev1.projector_info()

dev2 = shop.printer('laser', 'mono', '16ppm')
dev2.model_name = 'Принтер лазерный HP Laser 107r'
dev2.serial_num = '12345'
dev2.country = 'China'
dev2.printer_info()

dev3 = shop.scanner('Планшетный', 'A4', '4096x4096', '4ppm')
dev3.model_name = 'Сканер Epson Perfection V19'
dev3.serial_num = '222222'
dev3.country = 'Hungary'
dev3.scanner_info()