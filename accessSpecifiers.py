class Car:
    numberOfwheels = 4
    _color = "Black"
    __yearOfManufacture = 2017


class Bmw(Car):
    def __init__(self):
        print(f"Protected attributed color : '{self._color}'")


car = Car()
print("Public attribute numberOfWheels ", car.numberOfwheels)
bmw = Bmw()
print(f"Private attribute yearOfManufacture: '{car._Car__yearOfManufacture}'")
