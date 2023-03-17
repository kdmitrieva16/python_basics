# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см*число м толщины полотна.
# Проверить работу метода. Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
class Road:
    weight = None
    thickness = None

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

    def intake(self):
        self.weight = 25
        self.thickness = 0.05
        intake = self._length * self._width * self.weight * self.thickness
        print(
            f' Масса асфальта необходимая  для покрытия всего полотна - {intake} кг =  {intake/1000} т.')


all_road = Road(20, 5000)
all_road.intake()