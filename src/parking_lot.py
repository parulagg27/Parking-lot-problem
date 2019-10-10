
class Car:
    def __init__(self, reg_no, color):
        self.reg_no = reg_no
        self.color = color


class ParkingSpot:
    def __init__(self, slot_no=None, available=True):
        self.slot_no = slot_no
        self.car = None
        self.available = True


class ParkingLot(object):
    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, total_slots):
        total_slots = int(total_slots)

        if total_slots <= 0:
            return "Invalid number of Slots"

        for i in range(1, total_slots + 1):
            self.slots[i] = ParkingSpot(slot_no=i, available=True)
        return "Created a parking lot with %s slots" % total_slots

    def _parking_lot_created(self):
        if not self.slots:
            print("Create Parking lot first")
            return False
        return True

    def _find_nearest_available_slot(self):
        if not self._parking_lot_created:
            return
        available_slots = list(filter(lambda x: x.available, self.slots.values()))

        if not (available_slots):
            return None
        return sorted(available_slots, key=lambda x: x.slot_no)[0]


    def park(self, reg_no, color):
        if not self._parking_lot_created:
            return
        available_slot = self._find_nearest_available_slot()

        if available_slot is None:
            return "Sorry, parking lot is full"

        available_slot.car = Car(reg_no, color)
        available_slot.available = False
        return "Allocated slot number: %s" % available_slot.slot_no

    def leave(self, slot_number_to_be_freed):
        if not self._parking_lot_created:
            return

        slot_number_to_be_freed = int(slot_number_to_be_freed)
        slot_to_be_freed = self.slots[slot_number_to_be_freed]

        if slot_number_to_be_freed not in self.slots:
            return "Invalid Slot No. provided"

        if slot_to_be_freed.available and (slot_to_be_freed.car is None):
            return "No car present at Slot No. %s" % slot_number_to_be_freed

        slot_to_be_freed.car = None
        slot_to_be_freed.available = True
        return "Slot number %s is free" % slot_number_to_be_freed

    def status(self):
        if not self._parking_lot_created:
            return
        print("Slot No.\tRegistration No   \tColour")

        for slot in self.slots.values():
            if not slot.available and slot.car:
                print("{}   \t\t{}\t\t{}".format(slot.slot_no, slot.car.reg_no, slot.car.color))

    def exit():
        pass

    def registration_numbers_for_cars_with_colour(self, color):
        registration_numbers = []
        if not self._parking_lot_created:
            return

        for slot in self.slots.values():
            if not slot.available and slot.car and slot.car.color == color:
                registration_numbers.append(slot.car.reg_no)

        if not registration_numbers:
            return "Not found"
        return ', '.join(registration_numbers)

    def slot_numbers_for_cars_with_colour(self, color):
        slot_numbers = []
        if not self._parking_lot_created:
            return

        for slot in self.slots.values():
            if not slot.available and slot.car and slot.car.color == color:
                slot_numbers.append(str(slot.slot_no))

        if not slot_numbers:
            return "Not Found"
        return ', '.join(slot_numbers)

    def slot_number_for_registration_number(self, reg_no):
        if not self._parking_lot_created:
            return

        for slot in self.slots.values():
            if not slot.available and slot.car and slot.car.reg_no == reg_no:
                return slot.slot_no
        return "Not found"
