class vehicle:
    name = ""
    manufacturedYear = 2020

    def __init__(self, name, manufacturedYear):
        self.name = name
        self.manufacturedYear = manufacturedYear

    def car_data(self):
        print(self.name)

class typeOfVehicle(vehicle):
    vehicleType = ""

    def __init__(self, name, manufacturedYear, vehicleType):
        super().__init__(name, manufacturedYear)
        self.vehicleType = vehicleType

    def print_vehicleType(self):
        print(self.vehicleType) 


sample = typeOfVehicle("Honda", 2026, "EV")
print(sample)
sample.print_vehicleType()
sample.car_data()


