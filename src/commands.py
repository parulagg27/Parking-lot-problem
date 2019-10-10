from cmd import Cmd
from parking_lot import ParkingLot


parking_lot = ParkingLot()


class MyPrompt(Cmd):
    prompt = 'parkingLot> '

    def do_create_parking_lot(self, no_of_slots):
        params = no_of_slots.strip().split()
        if not len(params) == 1:
            print("Invalid no. of Arguments")
            return
        print(parking_lot.create_parking_lot(no_of_slots))


    def do_park(self, params):
        params = params.strip().split()
        # TODO: Handle cases when: Args not in order, upper-lowercase, incorrect car_no
        # TODO:- Handle case when: car already exists: TO avoid duplicaate slot allotment
        if not len(params) == 2:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.park(*params))


    def do_leave(self, slot_no):
        params = slot_no.strip().split()
        # TODO: Handle case when int(slot) is not valid, ex: slot_no=eight invalid
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.leave(slot_no))

    def do_status(self, line):
        if len(line):
            print("No Arguments required to check status. Type 'help' for guide")
        parking_lot.status()


    def do_registration_numbers_for_cars_with_colour(self, colour):
        params = colour.strip().split()
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.registration_numbers_for_cars_with_colour(colour))


    def do_slot_numbers_for_cars_with_colour(self, colour):
        params = colour.strip().split()
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.slot_numbers_for_cars_with_colour(colour))


    def do_slot_number_for_registration_number(self, reg_no):
        params = reg_no.strip().split()
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.slot_number_for_registration_number(reg_no))


    def do_exit(self, line):
        return True

    do_EOF = do_exit
