from read_input import parse_arguments, process_input


def main():
    # Parsing the argument which should be the input file
    file_name = parse_arguments()

    # Create the squad (list of rovers) from the content of the file
    squad = process_input(file_name)

    # Each rover will navigate the plateau and report its location
    for rover in squad:
        rover.navigate()
        rover.report_location()


# Launching the program:
main()
