# David Muñoz's SEATCode Challenge - User Guide
A squad of rovers explore the martian surface in the SEATCode Challenge

### CODE DOCUMENTATION:
In order to consult the code's documentation, download the proyect and open the file *./doc/html/index.html* in your browser

### PREREQUISITES:

[Download and Install Python 2.7](https://www.python.org/download/releases/2.7/) (note that Mac OS X 10.8 comes with Python 2.7 pre-installed by Apple)

### BASIC USAGE:
```
python main.py text_file_input
```
### INPUT

**text_file_input** should be a plain text file containing the setting up and instructions as stated in the challenge:

*"The first line of input is the upper‑right coordinates of the plateau, the
lower‑left coordinates are assumed to be 0,0. The rest of the input is
information pertaining to the rovers that have been deployed. Each
rover has two lines of input. The first line gives the rover’s position, and
the second line is a series of instructions telling the rover how to explore
the plateau. The position is made up of two integers and a letter
separated by spaces, corresponding to the x and y co‑ordinates and the
rover’s orientation. Each rover will be finished sequentially, which
means that the second rover won’t start to move until the first one has
finished moving."*

#### Example of the content a text file input (named test_case1_boundaries.txt):
```
9 4
2 3 E
M M R M M L L M
5 0 S
M M L M M M L M M M R M M M
```


### OUTPUT

The output of the application will contain 1 line for each rover defined with its final coordinates and heading.

#### Example output running the program using test_case1_boundaries.txt as input:

```
python main.py test_case1.txt
```
```
4 2 N
9 3 E
```

### DESIGN ASSUMPTIONS

The following assumptions were made in the design and development of the application:

-	The rovers can cross a position where another rover stays
-	The range of valid positions goes from (0,0) to (upper_limit_x, upper_limit_y)
-	If an incorrect movement instruction is detected, it will be reported and ignored
-	If an incorrect number of blank spaces are detected inside the position or movement strings, they will be ignored



