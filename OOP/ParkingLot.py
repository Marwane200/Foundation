'''
This systems implments the parking lot system design problem.
The Parking Lot contains the following components.

-Classes-
    ParkingLot: creates parking lot and manages cars parking
    ParkingSpot: initilizes a parking spot object with associated spot size
    Vehicle: Abstract class to create vehicles entities which can park in the parking lot
        Bike: Small vehicle implmentation
        Car: Medium vehicle implementation
        Truck: Large vehicle implmentation
'''

class parkingLot:
    '''
    PARKING LOT
    -Constructor-
    parkingLot: 
        - Creates a parkingLot object labeled by Zipcode
        - Empty spots are organized by a stack to find the closest spot in O(n) time
        - Taken spots are organized by a hashmap inorder for quick look up time

    -Functions-
    createLot:
        - Creates initial lot size divided evenly by small, medium, and large parking spots

    placeVehicle:
        - Based on car size it will return the closest spot on the proper stack as location for the vehicle
        - It will then add this spot to the hash map of parked cars with the key being the license plate 
    
    getVehicle:
        - This will return the spot id from the parked cars Hash Map
    '''
    def __init__(self, zipCode):
        #Parking Lot Identity
        self.zipCope = zipCode

        #Available Spots Stack
        self.smallStack = []
        self.mediumStack = []
        self.largeStack = []

        #Taken Spots
        self.parkedCars = {}
    
    # Creates Parking Lot Parking Spot Objects
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
    
    #Get Vehicle Class
    def getVehicle(self, plateNumber):
        spot = self.parkedCars.get(plateNumber)
        self.parkedCars.pop(plateNumber)
        print("Your car is located at spot: " + str(spot.id))

#Class for creating Parking Spot Objects
class parkingSpot:
    def __init__(self, id, size):
        self.id = id
        self.size = size


#Abstract Vehicle Class
class Vehicle:
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color

#Sub classes that inheret from the Vehicle
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
