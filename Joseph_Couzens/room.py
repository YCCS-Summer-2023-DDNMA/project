
class RoomImpl:


    def __init__(self, roomnum, sqfoot, maxOccupancy):
        self.sqr_feet = sqfoot
        self.room_number = roomnum
        self.occupants = []
        self.occupancy = maxOccupancy


    def add_occupant(self, name : str):
        if (len(self.occupants) >= self.occupancy):
            print("Cannot add occupant, max occupancy has been reached.")
        else:
            self.occupants.append(name)

    def change_max_occupancy(self, num):
        self.occupancy = num
        if (len(self.occupants) > self.occupancy):
            while(len(self.occupants) > self.occupancy):
                self.occupants.pop(len(self.occupants) - 1)
        
    def show_occupants(self):
        return self.occupants

    def get_sqr_feet(self):
        return self.sqr_feet
        

        
    
