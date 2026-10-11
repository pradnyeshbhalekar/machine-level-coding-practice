from enum import Enum

class VehicleType(Enum):
    SMALL = "SMALL"
    COMPACT = "COMPACT"
    LARGE = "LARGE"

my_size = VehicleType.SMALL
print(my_size.value)


class SpotType(Enum):
    SMALL = "SMALL"
    COMPACT = "COMPACT"
    LARGE = "LARGE"

class Spot:
    def __init__(self,spot_id,spot_type,is_occupied=False,current_vehicle=None):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = is_occupied
        self.current_vehicle = current_vehicle

    def assign_vehicle(self,vehicle):
        if self.is_occupied:
            raise Exception(f"Spot {self.spot_id} is already occupied")
        
        self.current_vehicle = vehicle
        self.is_occupied = True

    def remove_vehicle(self):
        if not self.is_occupied:
            raise Exception(f"Spot {self.spot_id} is already empty")
        self.current_vehicle = None
        self.is_occupied = False


class Vehicle:
    def __init__(self,vehicle_id,vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
    
class Floor:
    def __init__(self,floor_name):
        self.floor_name = floor_name
        self.spots = []
    
    def add_spot(self,spot):
        self.spots.append(spot)
    
    def find_spots(self,vehicle_type):
        for spot in self.spots:
            if not spot.is_occupied and spot.spot_type.value == vehicle_type.value:
                return spot
            else:
                return None
    

class ParkingLot:
    def __init__(self,name):
        self.name = name
        self.floors = []

    def add_floor(self,floor):
        self.floors.append(floor)
    
    def get_available_spots_by_type(self,vehicle_type):
        for floor in self.floors:
            spot = floor.find_spots(vehicle_type)
            return spot
        return None
    
    def park_vehicle(self,vehicle):
        spot = self.get_available_spot_by_type(vehicle.vehicle_type)
        if spot is None:
            raise Exception(f"Parking spot is full!")
        spot.assign_vehicle(vehicle)
        # next: create a Ticket here once that class exists, then return it

class Ticket:
    def __init__(self):
        
        

