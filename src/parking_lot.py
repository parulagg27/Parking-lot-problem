from collections import OrderedDict
from enum import Enum


class Car:
    def __init__(self, reg_no, color):
        self.reg_no = reg_no
        self.color = color


class ParkingSpot:
    def __init__(self, slot_no=None, available=True):
        self.slot_no = slot_no
        self.car = None
        self.available = True

    def assign_slot(self, car):
        self.car = car
        self.available = False

    def free_slot(self):
        self.car = None
        self.available = True


class ParkingLot:
    def __init__(self):
        self.slots = {}
        self.car_color_reg_number_mapper = {}
        self.car_color_slot_number_mapper = {}
        self.slot_reg_number_mapper = OrderedDict()


    def create_parking_lot(self, total_slots):
        total_slots = int(total_slots)

        if total_slots <= 0:
            return "Invalid number of Slots"
        for i in range(1, total_slots + 1):
            self.slots[i] = ParkingSpot(slot_no=i, available=True)

        return "Created a parking lot with %s slots" % total_slots


    def _find_nearest_available_slot(self):
        available_slots = list(filter(lambda x: x.available, self.slots.values()))

        if not (available_slots):
            return None
        return sorted(available_slots, key=lambda x: x.slot_no)[0]


    def park(self, reg_no, color):
        available_slot = self._find_nearest_available_slot()

        if available_slot is None:
            return "Sorry, parking lot is full"

        available_slot.car = Car(reg_no, color)
        available_slot.available = False
        return "Allocated slot number: %s" % available_slot.slot_no


    def leave(self, slot_to_be_freed):
        slot_to_be_freed = int(slot_to_be_freed)
        if slot_to_be_freed not in self.slots:
            return "Invalid Slot No. provided"

    def free_slot(self, slot_no):
        pass

    def status(self):
        pass

    def registration_numbers_for_cars_with_colour(self, color):
        pass

    def slot_numbers_for_cars_with_colour(self, reg_no):
        pass

    def slot_number_for_registration_number(self, color):
        pass

    def exit():
        pass
