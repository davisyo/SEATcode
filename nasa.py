class Plateau:
    def __init__(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit


class Rover:
    def __init__(self, initial_loc, movements, board):
        self.current_position_x = int(initial_loc[0])
        self.current_position_y = int(initial_loc[1])
        self.orientation = initial_loc[2]
        self.movements = movements
        self.board = board

    def rotate(self, direction):
        # Function to rotate the rover to the right or to the left
        if direction == 'R':
            if self.orientation == 'N':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'S'
            elif self.orientation == 'S':
                self.orientation = 'W'
            elif self.orientation == 'W':
                self.orientation = 'N'
        elif direction == 'L':
            if self.orientation == 'N':
                self.orientation = 'W'
            elif self.orientation == 'W':
                self.orientation = 'S'
            elif self.orientation == 'S':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'N'

    def advance(self):
        # Function to move forward taking into account the board limits
        if (self.orientation == 'N') & (self.current_position_y < self.board.y_limit):
            self.current_position_y = self.current_position_y + 1
        elif (self.orientation == 'E') & (self.current_position_x < self.board.x_limit):
            self.current_position_x = self.current_position_x + 1
        elif (self.orientation == 'S') & (self.current_position_y > 0):
            self.current_position_y = self.current_position_y - 1
        elif (self.orientation == 'W') & (self.current_position_x > 0):
            self.current_position_x = self.current_position_x - 1

    def navigate(self):
        position = 0
        for instruction in self.movements:
            position += 1
            if instruction == 'M':
                self.advance()
            elif (instruction == 'R') | (instruction == 'L'):
                self.rotate(instruction)
            elif True:
                print ("Detected not valid instruction: " + str(instruction) + " at position: " + str(position))

    def report_location(self):
        print (str(self.current_position_x) + " " + str(self.current_position_y) + " " + self.orientation)
