class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"{self.make}, {self.model}"


class Car(Vehicle):
    def __init__(self, model, make, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        info_with_fuel = super().get_info()
        return f"{info_with_fuel}, \nFuel type: {self.fuel_type}"


Car = Car('Porshe', '911turboS', 100)

print(Car.get_info())
