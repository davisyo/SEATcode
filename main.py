from read_input import parse_arguments, process_input


def main():
    # Parsing the argument which should be the input file
    args = parse_arguments()

    # Create the squad (list of rovers) from the content of the file
    squad = process_input(args)

    # Each rover will navigate the plateau and report its location
    for rover in squad:
        rover.navigate()
        rover.report_location()


# Launching the program:
main()
