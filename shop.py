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

    def move_dev(self, move_type, dev_count):

        if move_type == 'in': # перемещение на склад
            print(f'\n Операция: перемещение на склад {self.store_name} товара:')
            for key, value in dev_count.items():
                print(f'{key}: {value}')
                if key not in self.store_dev:
                    self.store_dev[key] = value
                else:
                    self.store_dev[key] += value
        elif move_type == 'out': # перемещение со склада
            print(f'\n Операция: перемещение со склада {self.store_name} товара:')
            for key, value in dev_count.items():
                print(f'{key}: {value}')
                # Здесь намеренно не обрабатываю ситуацию по контролю остатков, только вывожу предупреждение
                # об отсутствии, либо недостаточном количестве товара на складе
                if key not in self.store_dev:
                    print(f'Товар {key} отсутствует на складе! Перемещение со склада не будет выполнено!')
                else:
                    if self.store_dev[key] < value:
                        print(f'Товар {key} отсутствует на складе в нужном количестве! Перемещение со склада не будет выполнено!')
                    else:
                        self.store_dev[key] -= value

    def get_dev_count(self):
        print(f'\n Остатки товара на складе № {self.store_id} - {self.store_name}:')
        for key, value in self.store_dev.items():
            print(f'Устройство: {key}. Количество в остатке: {value}')


class devices():
    def __init__(self, model_name, serial_num, country):
        self.model_name = model_name    # наименование модели
        self.serial_num = serial_num    # серийный номер
        self.country = country          # страна-производитель

    def info(self):
        print(f'Наименование модели: {self.model_name}')
        print(f'Серийный номер: {self.serial_num}')
        print(f'Страна-производитель: {self.country}')

class printer(devices):
    def __init__(self, model_name, serial_num, country, printer_type, is_color, ppm):
        self.type = 'Принтер'
        self.printer_type = printer_type    # технология печати (матричный, струйный, лазерный)
        self.is_color = is_color            # цветной, монохромный
        self.ppm = ppm                      # скорость печати
        super().__init__(model_name, serial_num, country)

    def info(self):
        print(f'\nТип устройства: принтер')
        print(f'Технология печати: {self.printer_type}')
        print(f'Цветной/монохромный: {self.is_color}')
        print(f'Скорость печати: {self.ppm}')
        super().info()

class scanner(devices):
    def __init__(self, model_name, serial_num, country, scanner_type, paper_format, res, ppm):
        self.type = 'Сканер'
        self.scanner_type = scanner_type    # планшетный, ручной
        self.paper_format = paper_format    # формат (A0, A1, A2, A3, A4)
        self.res = res                      # разрешение
        self.ppm = ppm                      # скорость сканирования
        super().__init__(model_name, serial_num, country)

    def info(self):
        print(f'\nТип устройства: сканер')
        print(f'Тип сканера: {self.scanner_type}')
        print(f'Формат бумаги: {self.paper_format}')
        print(f'Разрешение: {self.res}')
        print(f'Скорость сканирования: {self.ppm}')
        super().info()

class projector(devices):
    def __init__(self, model_name, serial_num, country, projector_type, res, lumen):
        self.type = 'Проектор'
        self.projector_type = projector_type    # LCD, DLP, LCoS
        self.res = res                          # разрешение
        self.lumen = lumen                      # световой поток
        super().__init__(model_name, serial_num, country)

    def info(self):
        print(f'\nТип устройства: проектор')
        print(f'Тип проектора: {self.projector_type}')
        print(f'Разрешение: {self.res}')
        print(f'Световой поток: {self.lumen}')
        super().info()