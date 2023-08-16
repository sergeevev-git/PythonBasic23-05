from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: str = 1500
    started: bool = False
    fuel: float = 33.5
    fuel_consumption: float = 6.7

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Отсутствует топливо')

    def move(self, distance):
        total_distance = self.fuel / self.fuel_consumption
        if total_distance >= distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel('Недостаточно топлива')
