from parking_lot import ParkingLot
import sys
import os
import fileinput


parking_lot = ParkingLot()

command_params_len_mapper = {
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

    if not hasattr(parking_lot, command):
        return "Command not found"

    parking_operation = getattr(parking_lot, command)
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
        line = input()
        process_input(line)

    elif len(sys.argv) == 2:
        file_exists = process_file(sys.argv[1])
        if file_exists:
            for line in fileinput.input():
                process_input(line)
        # TODO: Handle case in better way when file doesn't exist

    else:
        print("Invalid number of arguments for given command")
