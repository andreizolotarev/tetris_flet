import math
import random
import flet as ft

class TetrisPiece:
    print('property')
    tetris_pieces = ['L','J','I','O','S','Z','T']

    def __init__(self, 
                 piece_type: str,
                 rows: int, 
                 columns: int,
                 grid):
        self.grid = grid
        self.piece_type = piece_type
        self.rows = rows
        self.columns = columns
        if piece_type == "S":
            self.position = [1, 2, 10, 11]
            self.default_color = ft.colors.RED_900
        if piece_type == "L":
            self.position = [0, 10, 20, 21]
            self.default_color = ft.colors.ORANGE_900
        if piece_type == "O":
            self.position = [0, 1, 10, 11]
            self.default_color = ft.colors.YELLOW_900
        if piece_type == "Z":
            self.position = [0, 1, 11, 12]
            self.default_color = ft.colors.GREEN_900
        if piece_type == "J":
            self.position = [1, 11, 21, 20]
            self.default_color = ft.colors.BLUE_900
        if piece_type == "I":
            self.position = [0, 10, 20, 30]
            self.default_color = ft.colors.INDIGO_900
        if piece_type == "T":
            self.position = [0, 1, 2, 11]
            self.default_color = ft.colors.PURPLE_900
        # place the piece above the board
        self.position = [i-(3*self.columns) for i in self.position]
        # place it randomly on columns
        rand_row_pos = random.randint(2, 6)
        self.position = [i+rand_row_pos for i in self.position]
        self.rotation_state = 0
        #self.gameboard = [[None for column in range(self.columns)] for row in range(self.rows)]
        self.next_tetris_piece = random.choice(TetrisPiece.tetris_pieces)

    def move_piece(self, direction, params=None):
        self.grid.add_next_piece(next_tetris_piece=self.next_tetris_piece)
        self.direction = direction
        self.params = params
        if direction == 'down':
            self.new_position = [pixel_id + self.columns for pixel_id in self.position.copy()]
            if self.check_collision_or_bottom():
                self.piece_landed(pixels_id=self.position)
            else:
                self.position = self.new_position.copy()
        
        
        if direction == 'left':
            self.new_position = [pixel_id - 1 for pixel_id in self.position.copy()]
            if not self.check_collision_or_bottom():
                self.position = self.new_position.copy()
       
        if direction == 'right':
            self.new_position = [pixel_id + 1 for pixel_id in self.position.copy()]
            if not self.check_collision_or_bottom():
                self.position = self.new_position.copy()
        
        self.grid.color_pixels(tetris_piece=self)
    
    def rotate_piece(self):
        if self.rotation_state == 0:
            if self.piece_type == 'L':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel - 1 + self.columns
                ]
            if self.piece_type == 'J':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - self.columns - 1,
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1
                ]
            if self.piece_type == 'I':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - 2,
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1
                ]
            if self.piece_type == 'S':
                pivot_pixel = self.position.copy()[0]
                self.new_position = [
                    pivot_pixel - 1 - self.columns,
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + self.columns
                ]
            if self.piece_type == 'Z':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel - 1 + self.columns
                ]
            if self.piece_type == 'T':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + self.columns
                ]

            
        if self.rotation_state == 1:
            if self.piece_type == 'L':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - self.columns - 1,
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + self.columns
                ]
            if self.piece_type == 'J':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel - self.columns + 1,
                    pivot_pixel,
                    pivot_pixel + self.columns
                ]
            if self.piece_type == 'I':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - 2*self.columns,
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + self.columns
                ]
            if self.piece_type == 'S':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel - self.columns + 1,
                    pivot_pixel - 1,
                    pivot_pixel
                ]
            if self.piece_type == 'Z':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - self.columns - 1,
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + 1
                ]
            if self.piece_type == 'T':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1
                ]

        if self.rotation_state == 2:
            if self.piece_type == 'L':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel + 1 - self.columns,
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1,
                ]
            if self.piece_type == 'J':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel + self.columns + 1
                ]
            if self.piece_type == 'I':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel + 2
                ]
            if self.piece_type == 'S':
                pivot_pixel = self.position.copy()[3]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel + 1 + self.columns
                ]
            if self.piece_type == 'Z':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - self.columns + 1,
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel + self.columns
                ]
            if self.piece_type == 'T':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel + self.columns
                ]


        if self.rotation_state == 3:
            if self.piece_type == 'L':
                pivot_pixel = self.position.copy()[2]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + self.columns,
                    pivot_pixel + self.columns + 1
                ]
            if self.piece_type == 'J':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + self.columns,
                    pivot_pixel + self.columns - 1
                ]
            if self.piece_type == 'I':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - self.columns,
                    pivot_pixel,
                    pivot_pixel + self.columns,
                    pivot_pixel + 2*self.columns
                ]
            if self.piece_type == 'S':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel + self.columns - 1,
                    pivot_pixel + self.columns
                ]
            if self.piece_type == 'Z':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + self.columns,
                    pivot_pixel + self.columns + 1
                ]
            if self.piece_type == 'T':
                pivot_pixel = self.position.copy()[1]
                self.new_position = [
                    pivot_pixel - 1,
                    pivot_pixel,
                    pivot_pixel + 1,
                    pivot_pixel + self.columns
                ]

        if not self.check_collision_or_bottom(rotation=True):
            self.position = self.new_position.copy()
            self.rotation_state = (self.rotation_state + 1) % 4
            self.grid.color_pixels(tetris_piece=self)


    def check_collision_or_bottom(self, rotation=None):
        '''
        return True if there is a collision, otherwise False
        '''
        # loop through each position of the piece, calc row and column of the position
        #print('check collision')
        for new_pixel_id, old_pixel_id in zip(self.new_position, self.position):
            #if new_pixel_id < 0:
                #return False
            if new_pixel_id >= 0:
                new_n_row = math.floor(new_pixel_id / self.columns)
                old_n_column = old_pixel_id % self.columns


                # reached the bottom
                if new_n_row >= self.rows:
                    return True

                # touched another blocked figure
                if new_pixel_id in self.grid.blocked_pixels:
                    return True

                # check if the piece is out of bounds 
                if self.direction == 'left':
                    new_n_column = old_n_column - 1
                    if new_n_column < 0:
                        return True
                
                if self.direction == 'right':
                    new_n_column = old_n_column + 1
                    if new_n_column >= self.columns:
                        return True
                
                if rotation:
                    new_n_column = new_pixel_id % self.columns
                    if old_n_column in list(range(self.columns))[:4] and new_n_column in list(range(self.columns))[-4:]:
                        return True
        else:
            return False


    
    def piece_landed(self, pixels_id):
        self.grid.color_blocked_pixel(pixels_to_add=pixels_id)
        self.params['frame_rate_ms'] = self.params['normal_frame_rate_ms']
        self.grid.clear_rows()
        self.recreate_new_piece()
        print('created', self.piece_type)


    def recreate_new_piece(self, piece_type=None):
        if piece_type:
            self = self.__init__(piece_type=piece_type, rows=self.rows, columns=self.columns, grid=self.grid)
        else:
            self = self.__init__(piece_type=self.next_tetris_piece, rows=self.rows, columns=self.columns, grid=self.grid)
        
        
    @classmethod
    def create_new_piece(cls, rows, columns, grid):
        piece_type = random.choice(cls.tetris_pieces)
        print('created', piece_type)
        return cls(piece_type=piece_type,
                   rows=rows,
                   columns=columns,
                   grid=grid)