"""This module contains the functions needed to obtain the input filename from the arguments, process it content
and initialize the Plateau and Rovers objects"""

import argparse                     # In order to parse the given arguments
from nasa import Plateau, Rover     # Classes definition in order to create the objects


def parse_arguments():
    """Parsing the argument which should be the input file"""

    parser = argparse.ArgumentParser(description='Obtain filepath from the arguments')
    parser.add_argument('file_path', action='store', type = str, help='path of the input file')

    args = parser.parse_args()
    return args


def process_input(args):
    """This function reads the content of the file and initializes the squad of rovers with the information provided.

    Blank spaces within the location and movement strings will be ignored.

    The structure of the file will be checked for errors.
    """

    # Open the file and store all lines in a list
    f = open(args.file_path, "r")
    input_list = f.readlines()

    # Check that the file is not empty, otherwise stop the program with an error message
    assert input_list, "The input file is empty"
    # The first line is the board limit
    board_limit = input_list.pop(0)
    # Remove blank spaces and end of line in the plateau limit string
    board_limit = board_limit.replace(" ", "")
    board_limit = board_limit.rstrip()
    # Create the board
    board = Plateau(board_limit[0], board_limit[1])

    # If the list is empty now, there aren't any rovers defined -> stop the program and raise an error
    assert input_list, "No rovers defined"
    # We create a list of rovers -> the squad
    squad = list()

    rover_count = 0
    # Now we read each 2 lines, create the rovers and add them to the fleet
    while input_list:

        rover_count += 1
        # Obtain initial position
        initial_position = input_list.pop(0)
        # If the list is empty now, the second line with the movements is empty -> stop the program and raise an error
        str_error = "No movement string defined for rover" + str(rover_count)
        assert input_list, str_error
        # Obtain movements string
        movements = input_list.pop(0)
        # Remove blank spaces and end of line in the position and movement string
        initial_position = initial_position.replace(" ", "")
        initial_position = initial_position.rstrip()
        movements = movements.replace(" ", "")
        movements = movements.rstrip()
        # With the gathered info, we create the rover and add it to the squad
        rover = Rover(initial_position, movements, board)
        squad.append(rover)

    return squad
