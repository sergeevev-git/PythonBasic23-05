from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(
        self, weight: int = 1500, fuel: int = 33.5, fuel_consumption: int = 6.7
    ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Отсутствует топливо")

    def move(self, distance):
        total_distance = self.fuel / self.fuel_consumption
        if total_distance >= distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel("Недостаточно топлива")
