class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def desc(self):
        longname = self.make + " " + self.model + " " + str(self.year)
        return longname.title()

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def update_odometer(self, b):
        if b >= self.odometer_reading:
            self.odometer_reading = b
        else:
            print("You cannot roll back an odometer!")

    def read_odometer(self):
        print("This is car " + str(self.odometer_reading) + " miles on it ")

a = Car("a4","audi",2022)
print(a.desc())
a.update_odometer(1500)
a.read_odometer()
a.increment_odometer(525)
a.read_odometer()