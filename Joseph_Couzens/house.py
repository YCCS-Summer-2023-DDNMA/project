import room

class HouseImpl:

    def __init__(self, room_list):
        self.sqr_footage = 0
        for room in room_list:
            self.sqr_footage += room.get_sqr_feet()
        self.rooms = room_list
    
    def get_rooms(self):
        return self.rooms

    def get_sqr_footage(self):
        return self.sqr_footage

master_bedroom = room.RoomImpl(1, 150, 3)
bedroom2 = room.RoomImpl(2, 80, 1)
bedroom3 = room.RoomImpl(3, 100, 2)
bathroom1 = room.RoomImpl(4, 50, 1)
master_bathroom = room.RoomImpl(5, 80, 2)
living_room = room.RoomImpl(5, 225, 10)
kitchen = room.RoomImpl(6, 200, 8)
test_house = HouseImpl([master_bedroom, bedroom2, bedroom3, bathroom1, master_bathroom, living_room, kitchen])
assert test_house.get_sqr_footage() == 885