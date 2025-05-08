from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(message)s")


# Абстрактний клас транспортного засобу
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Клас автомобіля
class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Engine start")


# Клас мотоцикла
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Engine running")


# Абстрактна фабрика транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")


# Фабрика для ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")


# Використання
if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_car("BMW", "320i")
    vehicle2.start_engine()

    vehicle3 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle3.start_engine()

    vehicle4 = eu_factory.create_motorcycle("Ducati", "Monster")
    vehicle4.start_engine()
