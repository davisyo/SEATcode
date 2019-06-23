"""Main file to run the application"""

from read_input import parse_arguments, process_input


def main():
    """Launching the SEATCode Challenge application.

        1: Parsing the argument which should be the input file path

        2: Create the squad (list of rovers) from the content of the file

        3: Each rover will navigate the plateau and report its location
        """

    # Parsing the argument which should be the input file path
    file_name = parse_arguments()

    # Create the squad (list of rovers) from the content of the file
    squad = process_input(file_name)

    # Each rover will navigate the plateau and report its location
    for rover in squad:

        rover.navigate()

        rover.report_location()


# Call to the main function:
if __name__ == '__main__':
    main()
