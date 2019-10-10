from parking_lot import ParkingLot
import sys
import os
import fileinput
from commands import MyPrompt


parking_lot_operations = ParkingLot()

parking_command_param_count_mapper = {
    "create_parking_lot": 1,
    "park": 2,
    "leave": 1,
    "status": '',
    "registration_numbers_for_cars_with_colour": 1,
    "slot_numbers_for_cars_with_colour": 1,
    "slot_number_for_registration_number": 1
}


def process_input(command_params):
    command_with_params = command_params.strip().split()
    command = command_with_params[0]
    params = command_with_params[1:]

    if not hasattr(parking_lot_operations, command):
        print("Command not found")
        return

    if len(params) is not parking_command_param_count_mapper[command]:
        print("Invalid no. of Arguments")
        return

    parking_operation = getattr(parking_lot_operations, command)
    std_out = parking_operation(*params)
    if std_out:
        print(std_out)


def process_file(given_file):
    if not os.path.exists(given_file):
        print("Given File %s doesn't exist" % given_file)
        return False
    return True


if __name__ == "__main__":

    if len(sys.argv) == 1:
        p = MyPrompt()
        p.cmdloop()

    elif len(sys.argv) == 2:
        file_exists = process_file(sys.argv[1])
        if file_exists:
            for line in fileinput.input():
                process_input(line)
        # TODO: Handle case in better way when file doesn't exist

    else:
        print("Invalid number of arguments for given command")
