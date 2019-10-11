import unittest
import env
from src import parking_lot


class TestParkingLot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parking = parking_lot.ParkingLot()
        cls.alloted_slot = 1

    def test_create_parking_lot(self):
        self.assertEqual(self.parking.create_parking_lot(0), "Invalid number of Slots")
        self.assertNotEqual(self.parking.create_parking_lot(-1), "Created a parking lot with -1 slots")

        total_slots = 6
        self.parking.create_parking_lot(total_slots)
        self.assertEqual(len(self.parking.slots), total_slots, msg="Wrong Parking lot created")


    def test_park(self):
        reg_no = "KA-01-HH-1234"
        colour = "White"

        if not self.parking.slots:
            self.assertEqual(self.parking.park(reg_no, colour), "Parking lot was not created", "Park failed")

        self.parking.park(reg_no, colour)

        # Verified if 1st slot that was alloted is still indicating availability or not
        self.assertFalse(self.parking.slots[self.alloted_slot].available, msg="Parking Failed")

        for slot in self.parking.slots.values():
            if not slot.available and slot.car:
                # checks if slot alloted properly or not
                self.assertEqual(slot.car.reg_no, reg_no, "Parking failed")
                self.assertEqual(slot.car.colour, colour, "Parking failed")

        # since parking lot isn't full, this condition should pass
        self.assertNotEqual(self.parking.park("KA-01-HH-7777", "Black"), "Sorry, parking lot is full")


    def test_leave(self):
        self.parking.leave(1)
        self.parking.status()
        self.assertTrue(self.parking.slots[self.alloted_slot].available, "Leave failed")

        self.assertEqual(self.parking.leave(7), "Slot No. doesn't exist")
        self.assertEqual(self.parking.leave(4), "No car present at Slot No. 4")

    def test_registration_numbers_for_cars_with_colour(self):
        self.assertEqual(self.parking.registration_numbers_for_cars_with_colour("Black"), "KA-01-HH-7777")
        self.assertEqual(self.parking.registration_numbers_for_cars_with_colour("Red"), "Not found")

    def test_slot_numbers_for_cars_with_colour(self):
        self.assertEqual(self.parking.slot_numbers_for_cars_with_colour("Black"), "2")
        self.assertEqual(self.parking.slot_numbers_for_cars_with_colour("Red"), "Not found")

    def test_slot_number_for_registration_number(self):
        self.assertEqual(self.parking.slot_number_for_registration_number("KA-01-HH-7777"), 2)
        self.assertEqual(self.parking.slot_number_for_registration_number("KA-01-HH-2701"), "Not found")

    @classmethod
    def tearDownClass(cls):
        del cls.parking


if __name__ == "__main__":
    unittest.main()
