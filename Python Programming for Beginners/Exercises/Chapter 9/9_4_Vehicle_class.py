class Vehicle:
      def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year

      def get_make(self):
            return self.make
      
      def get_model(self):
            return self.model
      
      def get_year(self):
            return self.year

class Car(Vehicle):
      def __init__(self, make, model, year):
            Vehicle.__init__(self, make, model, year)
            self.vehicleclass = 'Sedan'

      def get_type(self):
            return self.vehicleclass

class Truck(Vehicle):
      def __init__(self, make, model, year):
            Vehicle.__init__(self, make, model, year)
            self.vehicleclass = 'Truck'

      def get_type(self):
            return self.vehicleclass
      
print ("Now creating a car of type Truck that is a Ford F-150 from 2017.\n")

car01 = Truck('Ford','F150',2017)

car02 = Car('Toyota','Camry',1995)

print("Details of car in storage:\n")

print(car01.get_make(),car01.get_model(),car01.get_year(),car01.get_type())

print(car02.get_make(),car02.get_model(),car02.get_year(),car02.get_type())