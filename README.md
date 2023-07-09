# holbertonschool-AirBnB_clone
<p align="center"><img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="AirBnb  logo"></p>

## Descreption:
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---
## Installation
* Clone This Repo `git clone https://github.com/hug0-cstrs/holbertonschool-AirBnB_clone.git`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console.py` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Environment :computer:
The console was developed in Ubuntu 20.04 LTS using python3 (version 3.10.6)

## Available Command:
* quit and EOF to exit the program
* help for every Command
* create 
* show
* destroy
* all
* update
* count

## Repo Contents :clipboard:
This repository constains the following files:

|   **File**   |   **Description**   |
| :-------------- | :---------------------: |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |

## Usage :wrench:

|   **Method**   |   **Description**   |
| :-------------- | :---------------------: |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |

## Examples:
###### Example No.1
```
hug0@LAPTOP-25FUP3F5:~/holbertonschool-AirBnB_clone$ ./console.py 
(hbnb) create User
f1b97a02-2a02-4e10-a2be-79375c76777b
(hbnb) show User
** instance id missing **
(hbnb) show User f1b97a02-2a02-4e10-a2be-79375c76777b
[User] (f1b97a02-2a02-4e10-a2be-79375c76777b) {'id': 'f1b97a02-2a02-4e10-a2be-79375c76777b', 'created_at': datetime.datetime(2023, 7, 9, 14, 58, 32, 431010), 'updated_at': datetime.datetime(2023, 7, 9, 14, 58, 32, 431133)}
(hbnb) all User
["[User] (f1b97a02-2a02-4e10-a2be-79375c76777b) {'id': 'f1b97a02-2a02-4e10-a2be-79375c76777b', 'created_at': datetime.datetime(2023, 7, 9, 14, 58, 32, 431010), 'updated_at': datetime.datetime(2023, 7, 9, 14, 58, 32, 431133)}", "[User] (f1b97a02-2a02-4e10-a2be-79375c76777b) {'id': 'f1b97a02-2a02-4e10-a2be-79375c76777b', 'created_at': datetime.datetime(2023, 7, 9, 14, 58, 32, 431010), 'updated_at': datetime.datetime(2023, 7, 9, 14, 58, 32, 431133)}"]
(hbnb) destroy User f1b97a02-2a02-4e10-a2be-79375c76777b
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb) 
```

## Built with :gear:
Python3 (3.10.6)


## Authors
Hugo Castéras - [Github](https://github.com/hug0-cstrs)

Noah Vernhet - [Github](https://github.com/truuue)

