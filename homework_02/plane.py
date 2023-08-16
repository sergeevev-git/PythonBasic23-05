"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, advance_cargo: int):
        if self.cargo + advance_cargo <= self.max_cargo:
            self.cargo += advance_cargo
        else:
            raise CargoOverload('Перегруз')

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
