# task 1

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def convert(cls, obj):
        obj.data = obj.data.split('-')
        return obj.data

    @staticmethod
    def right(x):
        d, m, y = [int(i) for i in x.data]
        if 1 <= d <= 31 and 1 <= m <= 12 and 1 <= y <= 2022:
            return True
        else:
            return False

d = Data('12-21-2001')
print(d.convert(d))
print(d.right(d))

# task 2

class Calc:
    def __init__(self, div, den):
        self.div, self.den = div, den

    @staticmethod
    def examination(div, den):
        if den == 0:
            print('Деление на ноль')
        else:
            print(div / den)

Calc.examination(10, 0)

# task 3

class Num:
    def __init__(self, *args):
        self.new_list = []

    def enter(self):

        while True:
            num = input('Введите значение: ')

            if num.isdigit():
                self.new_list.append(int(num))
                print(f'{self.new_list} \n ')

            elif num.isalpha():
                print(f"Введена строка")

            elif num == 'stop':
                break

n = Num(1)
n.enter()

# task 4, 5, 6

class StoreMashines:
    def __init__(self, *args):
        self.my_store = []

    def __str__(self):
        ret = ""
        i = 0
        while i < len(self.my_store):
            ret += self.my_store[i].type_class() + ": " + str(self.my_store[i]) + '\n'
            i += 1
        return ret


class OfficeEquipment:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} по цене {self.price} в количестве {self.quantity}'

    def __add__(self, other):
        return str(self) + other

    @classmethod
    def reception(cls):
        while True:
            try:
                unit = input(f'Введите наименование ')
                if not unit.isalpha():
                    raise Exception
                unit_p = int(input(f'Введите цену за ед '))
                unit_q = int(input(f'Введите количество '))
                break
            except Exception:
                print("Ошибка")
        per = cls(unit, unit_p, unit_q)
        sm.my_store.append(per)
        return per


class Printer(OfficeEquipment):
    def type_class(self):
        return 'Printer'

    def to_print(self):
        print(f'Данные для принтера: {self}')


class Scanner(OfficeEquipment):
    def type_class(self):
        return 'Scanner'

    def to_scan(self):
        print(f'Данные для сканера: {self}')


class Copier(OfficeEquipment):
    def type_class(self):
        return 'Copier'

    def to_copier(self):
        print(f'Данные для ксерокса: {self}')


sm = StoreMashines()

while True:
    inp = input('Enter Q to exit or p/s/c')
    if inp.lower() == "p":
        print("Введите данные для Принтера")
        pr = Printer.reception()
        pr.to_print()
    elif inp.lower() == "s":
        print("Введите данные для Сканера")
        sc = Scanner.reception()
        sc.to_scan()
    elif inp.lower() == "c":
        print("Введите данные для Ксерокса")
        cp = Copier.reception()
        cp.to_copier()
    elif inp.lower() == "q":
        break

print(sm)

# task 7

class Compl:
    def __init__(self, one, two, *args):
        self.one = one
        self.two = two
        self.sum = 'one + two * i'

    def __add__(self, other):
        print(f'Сумма чисел: ')
        return f'compl = {self.one + other.one} + {self.two + other.two} * i'

    def __mul__(self, other):
        print(f'Произведение чисел: ')
        return f'compl = {self.one * other.one - (self.two * other.two)} + {self.two * other.one} * i'

    def __str__(self):
        return f'compl = {self.one} + {self.two} * i'


compl = Compl(1, -2)
compl2 = Compl(1, 2)
print(compl)
print(compl + compl2)
print(compl * compl2)



