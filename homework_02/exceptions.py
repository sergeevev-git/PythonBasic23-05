"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class MyException(Exception):
    pass


class LowFuelError(MyException):
    pass


class NotEnoughFuel(MyException):
    pass


class CargoOverload(MyException):
    pass
