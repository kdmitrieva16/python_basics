# реализовать дескрипторы для любых двух классов

class NonStr:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Должно иметь строковый тип!")
        instance.__dict__[self.my_attr] = value


class Worker:
    name = NonStr()
    surname = NonStr()
    position = NonStr()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


manager = Position(5, 'Ivanov', 'manager', 1000, 200)
print(manager.get_full_name(), manager.get_total_income())
