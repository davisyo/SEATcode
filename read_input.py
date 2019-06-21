import argparse
from nasa import Plateau, Rover


def parse_arguments():
    # Parsing the argument which should be the input file
    parser = argparse.ArgumentParser(description='Read input file')
    parser.add_argument('file_path',
                        action='store',
                        type = str,
                        help='path of the input file')

    args = parser.parse_args()
    return args


def process_input(args):
    # Open the file and store all lines in a list
    f = open(args.file_path, "r")
    input_list = f.readlines()

    # Check that the list is not empty
    if input_list:
        # The first line is the board limit
        board_limit = input_list.pop(0)
        # Remove blank spaces and end of line in the position and movement string
        board_limit = board_limit.replace(" ", "")
        board_limit = board_limit.rstrip()
        board = Plateau(board_limit[0], board_limit[1])
        # We create a list of rovers -> the fleet
        fleet = list()

        # Now we read each 2 lines, create the rovers and add them to the fleet
        while input_list:
            initial_position = input_list.pop(0)
            movements = input_list.pop(0)
            # Remove blank spaces and end of line in the position and movement string
            initial_position = initial_position.replace(" ", "")
            initial_position = initial_position.rstrip()
            movements = movements.replace(" ", "")
            movements = movements.rstrip()
            rover = Rover(initial_position, movements, board)
            fleet.append(rover)

    return fleet
