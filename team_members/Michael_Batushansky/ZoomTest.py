import unittest
from Zoom import Zoom

class ZoomTestCase(unittest.TestCase):
    def setUp(self):
        attendees = [
            {'name': 'Misha', 'email': 'Misha@Yeshiva.com'},
            {'name': 'Mike', 'email': 'Mike@Gmail.com'},
            {'name': 'Michael', 'email': 'Michael@Yahoo.com'}
        ]
        self.zoom = Zoom("10:00 AM", "Team Meeting", attendees, "Weekly", "1 hour")

    def test_get_email(self):
        email = self.zoom.get_email("Misha")
        self.assertEqual(email, "Misha@Yeshiva.com")


    def test_nonexistent_name_withGet(self):
        email = self.zoom.get_email("David")
        self.assertIsNone(email)

    def test_set_time(self):
        self.zoom.set_time("10:00 AM")
        self.assertEqual(self.zoom.get_time(), "10:00 AM")

    def test_set_frequency(self):
        self.zoom.set_frequency("Daily")
        self.assertEqual(self.zoom.get_frequency(), "Daily")

    def test_get_nonexistent_attendee_email(self):
        email = self.zoom.get_email("Moshe")
        self.assertIsNone(email)

#not fully sure why i need, but unit tests did not run othewise
if __name__ == '__main__':
    unittest.main()
