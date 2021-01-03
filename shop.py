# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python

class store():
    def __init__(self, store_id, store_name, address, main_person, store_dev):
        self.store_id = store_id        # id-склада
        self.store_name = store_name    # название склада
        self.address = address          # адрес
        self.main_person = main_person  # ответственный
        self.store_dev = store_dev      # хранилище остатков товаров на складе

    def store_info(self):
        print(f'\nid-склада: {self.store_id}')
        print(f'Название склада: {self.store_name}')
        print(f'Адрес: {self.address}')
        print(f'Ответственный: {self.main_person}')

    def income_dev(self, dev_count):
        # self.to_store_id = to_store_id
        self.dev_count = dev_count  # self.dev_count = {name_dev1: count_dev1, name_dev2: count_dev2, ... name_dev_n: count_dev_n}

        for key, value in self.dev_count.items():
            if key not in self.store_dev:
                self.store_dev[key] = value
            else:
                self.store_dev[key] += value

    def get_dev_count(self):
        print(f'\n Остатки товара на складе {self.store_id} {self.store_name}:')
        for key, value in self.store_dev.items():
            print(f'Устройство: {key}. Количество в остатке: {value}')


    def move_dev(self, to_store_id, dev_count):
        pass


class devices():
    def __init__(self, model_name, serial_num, country):
        self.model_name = model_name    # наименование модели
        self.serial_num = serial_num    # серийный номер
        self.country = country          # страна-производитель

    def devices_info(self):
        print(f'Наименование модели: {self.model_name}')
        print(f'Серийный номер: {self.serial_num}')
        print(f'Страна-производитель: {self.country}')

class printer(devices):
    def __init__(self, printer_type, is_color, ppm):
        self.type = 'Принтер'
        self.printer_type = printer_type    # технология печати (матричный, струйный, лазерный)
        self.is_color = is_color            # цветной, монохромный
        self.ppm = ppm                      # скорость печати

    def printer_info(self):
        print(f'\nТип устройства: принтер')
        print(f'Технология печати: {self.printer_type}')
        print(f'Цветной/монохромный: {self.is_color}')
        print(f'Скорость печати: {self.ppm}')
        super().devices_info()

class scanner(devices):
    def __init__(self, scanner_type, paper_format, res, ppm):
        self.type = 'Сканер'
        self.scanner_type = scanner_type    # планшетный, ручной
        self.paper_format = paper_format    # формат (A0, A1, A2, A3, A4)
        self.res = res                      # разрешение
        self.ppm = ppm                      # скорость сканирования

    def scanner_info(self):
        print(f'\nТип устройства: сканер')
        print(f'Тип сканера: {self.scanner_type}')
        print(f'Формат бумаги: {self.paper_format}')
        print(f'Разрешение: {self.res}')
        print(f'Скорость сканирования: {self.ppm}')
        super().devices_info()

class projector(devices):
    def __init__(self, projector_type, res, lumen):
        self.type = 'Проектор'
        self.projector_type = projector_type    # LCD, DLP, LCoS
        self.res = res                          # разрешение
        self.lumen = lumen                      # световой поток

    def projector_info(self):
        print(f'\nТип устройства: проектор')
        print(f'Тип проектора: {self.projector_type}')
        print(f'Разрешение: {self.res}')
        print(f'Световой поток: {self.lumen}')
        super().devices_info()