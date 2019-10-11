# GOJEK - Parking Lot Problem

The car parking lot project for Automatic ticekting system has been written in <u>__Python__</u>


## Source Code: 
present in ```functional_spec/src``` folder

## Components/Classes Involved

### 1. ParkingLot

source: ```functional_spec/src/parking_lot```
It is the main component to initialize parking Lot.
Each parking lot consists of information about total slot capacity and occupied/avaialble slots information.

The ```fields``` in parking object include: 

* ```slots```: dictionary with keys = slot_no, values = Parking Slot object info for particular spot

Parking object has ```methods```:
1.  __init__(): To initialize parking_lot object with empty slot size
1. ```create_parking_lot()```: Creates parking lot with given no.of slots
1.  ```_find_nearest_available_slot()```: returns nearest available parking slot
1.  ```park()```: adds new car with given reg_no and color into nearest available slot
1.  ```leave()```: Removes car from given Slot No. provided car is present there.
1.  ```status()```: gives status of slots occupied inside parking lot
1.  ```registration_numbers_for_cars_with_colour()```: Returns registration no. of all cars present inside lot with given color
1. ```slot_numbers_for_cars_with_colour()```: Returns slot of numbers of all cars inside parking lot with given color
1. ```slot_number_for_registration_number()```: Returns slot of car inside with a particular reg.no

### 2. Car
source: ```functional_spec/src/parking_lot```

This class contains fields regarding given characteristics of Car:
1. reg_no: Registration No
2. colour: Car Colour

### 3. ParkingSpot
source: ```functional_spec/src/parking_lot.py```
This class contains fields regarding characteristics/status of a particular spot inside parking Lot, as specified in given problem statement.

The fields involved are:
1. slot_no: Slot number
2. avaialable: indicates status of parking lot, whether it is available or not
3. car: contains Car object and all it's details if slot is occupied


### 4. Commands:

source: ```functional_spec/src/commands.py```

It contains set of commands to control the lifescycle of the above stated components


## Application Setup
Run bash setup in bin directory:```parking_lot $ bin/setup```

The command will automatically build project, install dependency if any and run unit tests contained in the file bin/run_functional_tests

This application is fully controlled by command. Run bash parking_lot in bin directory with 2 options:

The inputs commands are expected and taken from the file specified
`parking_lot $ bin/parking_lot [input_filepath]`

Or start the program in interactive mode.
`parking_lot $ bin/parking_lot`


## Commands List:
Commands can be run both in interactive mode as well by inputting them via text file as stated above.

```parking_lot> create_parking_lot [capacity]```

Initializes parking lot with given slot capacity. This command must be run first to initialize the parking lot.

```parking_lot> park [car_registration_number] [car_color]```

The Car with given registration number and color alloted in nearest available parking slot.
Valid registration number example: ```DL-12-AA-9999``` 
If success, program will print ```Allocated slot number: [nearest_slot_number]```. 
If failed, (parking lot is full) will print ```Sorry, parking lot is full```

```parking_lot> leave [slot_number]```

The slot is made available again after the car leaves the parking lot.
It requries slot_number of car going out/leaving as it's parameter

```parking_lot> status``` 

For print parking area status in table format. Slot No.|  Registration No | Colour

```parking_lot> registration_numbers_for_cars_with_colour [car_color] ```

It prints all registration numbers of all cars with given ```colour```, present inside parking_lot


```parking_lot> slot_numbers_for_cars_with_colour [car_color] ```

It prints all slot numbers with specific car color for cars parked inside lot.

```parking_lot> slot_number_for_registration_number [car_registration_number] ```

It prints slot number of car whose registration number is given, provided car is present inside parking lot.
