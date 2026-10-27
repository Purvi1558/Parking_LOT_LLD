from .Vehicle import Vehicle
from ..enums.VehicleType import VehicleType

class Car(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.CAR)