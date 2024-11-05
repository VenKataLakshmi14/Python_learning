class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 80

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def drive(self, miles):
        self.mileage += miles
        print(f"Driving {miles} miles. Total mileage: {self.mileage} miles.")


my_car = Car("Toyota", "Camry", 2022)
my_car.display_info()
my_car.drive(int(input()))