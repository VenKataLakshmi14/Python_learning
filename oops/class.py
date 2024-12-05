class car:
    def __init__(self,carname,no_of_wheels,no_of_airbags):
        print("This is constructor!")
        self.carname=carname
        self.no_of_wheels=no_of_wheels
        self.no_of_airbags=no_of_airbags
        
        
    def __str__(self):
        return (self.carname)
    def moveforward(self):
        print("car is moving")
        
    def movebackward(self):
        print("car is moving backward")
        
#Instance of the class
car1=car("bmw",5,6)

print(car1.carname,car1.no_of_wheels,car1.no_of_airbags)

#create second instance of the class
car2=car("Audi",4,6)
print(car2.carname,car2.no_of_wheels,car2.no_of_airbags)
car2.moveforward()







        