# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 8. Задание 5:
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на
# склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.
import shop

s1 = shop.store(1, 'Основной склад', 'ул. Ленина, 1', 'Иванов И.И.', {})
s1.store_info()

s2 = shop.store(2, 'Магазин-1', 'ул. Московская, 1', 'Петров П.П.', {})
s2.store_info()

s3 = shop.store(3, 'Магазин-2', 'ул. Ломоносова, 1', 'Сидоров С.С.', {})
s3.store_info()

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

s1.income_dev({dev1.model_name: 2, dev2.model_name: 4, dev3.model_name:5})
s1.get_dev_count()
s1.income_dev({dev2.model_name: 1, dev3.model_name: 1, dev1.model_name: 2})
s1.get_dev_count()

s2.income_dev({dev1.model_name: 1, dev2.model_name: 1, dev3.model_name:1})
s2.get_dev_count()

s3.income_dev({dev2.model_name: 2, dev3.model_name: 2, dev1.model_name: 2})
s3.get_dev_count()
