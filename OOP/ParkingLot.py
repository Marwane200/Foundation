class parkingLot:
    def __init__(self, zipCode):
        #Parking Lot Identity
        self.zipCope = zipCode

        #Available Spots Stack
        self.smallStack = []
        self.mediumStack = []
        self.largeStack = []

        #Taken Spots
        self.parkedCars = {}
    
    def createLot(self, num):
        for i in range(num):
            self.smallStack.append(parkingSpot(i,'S'))
            self.mediumStack.append(parkingSpot(num+i, 'M'))
            self.largeStack.append(parkingSpot((2*num)+i,'L'))
        

    
    #Place Vehicle class 
    def placeVehicle(self, Vehicle):
        size = Vehicle.size
        if size == 'S':
            self.parkedCars[Vehicle.licensePlate]=self.smallStack.pop(0)
        elif size == 'M':
            self.parkedCars[Vehicle.licensePlate]=self.mediumStack.pop(0)
        else:
            self.parkedCars[Vehicle.licensePlate]=self.largeStack.pop(0)
    
    def getVehicle(self, plateNumber):
        spot = self.parkedCars.get(plateNumber)
        self.parkedCars.pop(plateNumber)
        print("Your car is located at spot: " + str(spot.id))

#Class for creating parkingSpots
class parkingSpot:
    def __init__(self, id, size):
        self.id = id
        self.size = size


#Abstract Vehicle Class
class Vehicle:
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color

#Sub Classes that inheret from the Vehicle
class Bike(Vehicle):
    def __init__(self, plate, color):
        super().__init__(plate, color)
        self.size = 'S'

class Car(Vehicle):
    def __init__(self, plate, color):
        super().__init__(plate, color)
        self.size = 'M'

class Truck(Vehicle):
    def __init__(self, plate, color):
        super().__init__(plate, color)
        self.size = 'L'


#Test Cases
bike1 = Bike("AB12345","Blue")
Truk1 = Truck("ABDE2","White")
print(bike1.color)

Lot1 = parkingLot('011512')
Lot1.createLot(5)
Lot1.placeVehicle(bike1)
Lot1.placeVehicle(Truk1)
Lot1.getVehicle(bike1.licensePlate)
Lot1.getVehicle(Truk1.licensePlate)
