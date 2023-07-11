import room
import unittest

class RoomTests(unittest.TestCase):

    def test_room_basic(self):
        test_room = room.RoomImpl(10, 300, 2)
        test_room.add_occupant("Bob")
        assert test_room.show_occupants() == ["Bob"]
        test_room.add_occupant("Sally")
        assert test_room.show_occupants() == ["Bob", "Sally"]
        test_room.add_occupant("No Room For Me")
        assert test_room.show_occupants() == ["Bob", "Sally"]

        assert test_room.get_sqr_feet() == 300

    def test_room_occupant_overload(self):
        test_room = room.RoomImpl(10, 300, 3)
        test_room.add_occupant("Bob")
        assert test_room.show_occupants() == ["Bob"]
        test_room.add_occupant("Sally")
        assert test_room.show_occupants() == ["Bob", "Sally"]
        test_room.add_occupant("Jimothy")
        assert test_room.show_occupants() == ["Bob", "Sally", "Jimothy"]
        test_room.change_max_occupancy(1)
        assert test_room.show_occupants() == ["Bob"]