from cmd import Cmd
from parking_lot import ParkingLot


parking_lot = ParkingLot()


class CLI_Prompt(Cmd):
    prompt = 'parkingLot> '

    def do_create_parking_lot(self, no_of_slots):
        """
        Initializes parking lot with given slot capacity.
        This command must be run first to initialize the parking lot.
        :params no_of_slotS: Total Slot capacity of parking lot
        """
        params = no_of_slots.strip().split()
        if not len(params) == 1:
            print("Invalid no. of Arguments")
            return
        print(parking_lot.create_parking_lot(no_of_slots))


    def do_park(self, params):
        """
        The Car with given registration number and color alloted in nearest available parking slot.
        It needs 2 parameters, i.e.,park [car_registration_number] [car_color]
        Valid registration number example: DL-12-AA-9999
        If success, program will print Allocated slot number: [nearest_slot_number].
        If failed, (parking lot is full) will print Sorry, parking lot is full
        """
        params = params.strip().split()
        if not len(params) == 2:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.park(*params))


    def do_leave(self, slot_no):
        """
        The slot is made available again after the car leaves the parking lot.
        :params slot_no: Slot Number of Parking Lot to be freed
        """
        params = slot_no.strip().split()
        # TODO: Handle case when int(slot) is not valid, ex: slot_no=eight invalid
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.leave(slot_no))

    def do_status(self, line):
        """
        It prints the parking area status in table format. 
        Slot No.| Registration No | Colour
        """
        if len(line):
            print("No Arguments required to check status. Type 'help' for guide")
        parking_lot.status()


    def do_registration_numbers_for_cars_with_colour(self, colour):
        """
        It prints all registration numbers of all cars with given colour,
        present inside parking_lot.
        :params colour: Car colour for Cars present in Parking Lot
        """
        params = colour.strip().split()
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.registration_numbers_for_cars_with_colour(colour))


    def do_slot_numbers_for_cars_with_colour(self, colour):
        """
        It prints all slot numbers with specific car colour for cars parked inside lot.
        :params colour: Car colour for Cars present in Parking Lot
        """
        params = colour.strip().split()
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.slot_numbers_for_cars_with_colour(colour))


    def do_slot_number_for_registration_number(self, reg_no):
        """
        It prints slot number of car whose registration number is given,
        provided car is present inside parking lot.
        :params reg_no: Car Registration Number
        """
        params = reg_no.strip().split()
        if not len(params) == 1:
            print("Invalid no of Arguments. Type 'help' for guide")
            return
        print(parking_lot.slot_number_for_registration_number(reg_no))


    def do_exit(self, line):
        """
        Exits the interactive command shell if "exit" is typed and entered
        or "Ctrl+D" is pressed (indicating EOF)
        """
        return True

    do_EOF = do_exit
