# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 8. Задание 4:
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для
# приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

import shop

dev1 = shop.projector(1, 'Проектор Philips NeoPix Easy+ серебристый', '111111', 'China', 'LCD', '800x600', 10000)
dev1.info()

dev2 = shop.printer(2, 'Принтер лазерный HP Laser 107r', '12345', 'China', 'laser', 'mono', '16ppm')
dev2.info()

dev3 = shop.scanner(3, 'Сканер Epson Perfection V19', '222222', 'Hungary', 'Планшетный', 'A4', '4096x4096', '4ppm')
dev3.info()