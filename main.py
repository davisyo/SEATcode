from read_input import parse_arguments, process_input


def main():
    # Parsing the argument which should be the input file
    args = parse_arguments()

    # Create the fleet (list of rovers) from the content of the file
    fleet = process_input(args)

    for rover in fleet:
        rover.navigate()
        rover.report_location()


# Launching the program:
main()
