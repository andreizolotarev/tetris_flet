#flet run tetris_flet/tetris.py --web --port 8888
import flet as ft
import math
import time
import random

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

class Buttons(ft.UserControl):
    def __init__(self, tetris_piece, params):
        super().__init__()
        self.tetris_piece = tetris_piece
        self.params = params

    def move_right(self, e: ft.ControlEvent):
        self.tetris_piece.move_piece(direction='right')
        self.update()

    def move_left(self, e: ft.ControlEvent):
        self.tetris_piece.move_piece(direction='left')
        self.update()

    def make_rotation(self, e: ft.ControlEvent):
        self.tetris_piece.rotate_piece()
        self.update()

    def drop_piece(self, e: ft.ControlEvent):
        self.params['frame_rate_ms'] = 50

    def build(self):
        buttons_row = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                             wrap=True, spacing=20,
                             controls=[ft.OutlinedButton(icon=ft.icons.ARROW_BACK_IOS,
                                                         on_click=self.move_left,
                                                         width=50, height=50),
                                       ft.OutlinedButton(icon=ft.icons.ARROW_FORWARD_IOS,
                                                         on_click=self.move_right,
                                                         width=50, height=50),
                                       ft.OutlinedButton(icon=ft.icons.ARROW_FORWARD_IOS,
                                                         rotate=ft.Rotate(angle=0.5 * math.pi),
                                                         on_long_press=self.drop_piece,
                                                         width=50, height=50),
                                       ft.OutlinedButton(icon=ft.icons.ROTATE_90_DEGREES_CW_SHARP,
                                                         on_click=self.make_rotation,
                                                         width=50, height=50),
                                       ])
        return buttons_row

class Grid(ft.UserControl):
    def __init__(self, params, rows: int = 20, columns: int = 10):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.total = rows * columns
        self.params = params
        self.colored_pixels = []
        self.blocked_pixels = []
        self.cleared_lines = 0
        self.level = 0
        self.default_color = ft.colors.GREY_800
    
    def color_pixels(self, tetris_piece):
        for pixel_id in range(self.rows * self.columns)[::-1]:
            if pixel_id in tetris_piece.position and pixel_id not in self.blocked_pixels:
                self.pixels[pixel_id].bgcolor = tetris_piece.default_color
            if pixel_id not in tetris_piece.position and pixel_id not in self.blocked_pixels:
                self.pixels[pixel_id].bgcolor = self.default_color
        self.colored_pixels = tetris_piece.position.copy()
        self.tetris_piece = tetris_piece
        self.update()
    
    def color_blocked_pixel(self, pixels_to_add=None, clear_line=None):
        if pixels_to_add:
            for pixel_id in pixels_to_add:
                self.blocked_pixels.append(pixel_id)
        for pixel_id in range(self.rows * self.columns)[::-1]:
            if pixel_id not in self.blocked_pixels:
                self.pixels[pixel_id].bgcolor = self.default_color
            if pixel_id in self.blocked_pixels and not clear_line:
                self.pixels[pixel_id].bgcolor = self.pixels[pixel_id].bgcolor
            if pixel_id in self.blocked_pixels and clear_line and self.pixels[pixel_id-self.columns].bgcolor != self.default_color:
                self.pixels[pixel_id].bgcolor = self.pixels[pixel_id-self.columns].bgcolor

        self.update()
        

    def have_space(self):
        if len(self.blocked_pixels)>0 and min(self.blocked_pixels) < self.columns:
            return False
        else:
            return True
    
    def clear_rows(self):
        cleared_rows = 0
        # for each row from bottom to top
        for n_row in range(self.rows)[::-1]:
            clear_row = True
            # check that all pixels in the row are blocked
            for pixel_id in range(n_row*self.columns, n_row*self.columns+self.columns):
                if pixel_id not in self.blocked_pixels:
                    # if the pixel is not blocked move to the next row
                    clear_row = False
                    break
            if clear_row == True: 
                pixels_to_drop = list(range(n_row*self.columns, n_row*self.columns+self.columns))
                # remove line with pixels
                self.blocked_pixels = [pixel_id for pixel_id in self.blocked_pixels if pixel_id not in pixels_to_drop]
                self.color_blocked_pixel()
                # shift down by row (add n pixels in row to all pixels above cleared line)
                self.blocked_pixels = [pixel_id + self.columns if pixel_id < pixels_to_drop[0] else pixel_id for pixel_id in self.blocked_pixels ]
                self.color_blocked_pixel(clear_line=True)
                cleared_rows += 1
                self.cleared_lines += 1
                self.current_score.value = f'Score: {self.cleared_lines}'
                if self.cleared_lines % 2 == 0:
                    self.level += 1
                    self.current_level.value = f'Level: {self.level}'
                    if self.params['frame_rate_ms'] > 50 and self.params['normal_frame_rate_ms'] > 50:
                        self.params['frame_rate_ms'] -= 50
                        self.params['normal_frame_rate_ms'] -= 50
                self.update()
        if cleared_rows > 0:
            self.clear_rows()

    def add_next_piece(self, next_tetris_piece):
        self.next_piece.value = f'Next: {next_tetris_piece}'
        self.update()

    def build(self):
        print('build')
        self.view = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
        # status bar
        self.current_level = ft.Text(value=f'Level: {self.level}')
        self.current_score = ft.Text(value=f'Score: {self.cleared_lines}')
        self.next_piece = ft.Text(value=f'Next:  ')
        self.view.controls.append(ft.Row(controls=[self.current_level, 
                                                   self.current_score,
                                                   self.next_piece],
                                         alignment=ft.MainAxisAlignment.CENTER,
                                         spacing=50))
        # grid with pixels
        self.pixels = [ft.Container(content=ft.Text(value=f'{i:03}', color=self.default_color, opacity=0), alignment=ft.alignment.center, bgcolor=self.default_color, border_radius=2) for i in range(self.total)]
        rows = [ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=2) for i in range(self.rows)]
        self.view.controls += rows
            
        for idx in range(self.total):
            n_row = math.floor(idx / self.columns)
            row = rows[n_row]
            row.controls.append(self.pixels[idx])

        # Buttons
        self.view.controls.append(ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=0))
        return self.view

class Tetris(ft.UserControl):
    def __init__(self, rows=20, columns=10):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.params = {'frame_rate_ms': 400, 'normal_frame_rate_ms': 400}
    
    def did_mount(self):
        self.running = True
        self.page.run_thread(self.play_tetris)
    
    def will_unmount(self):
        self.running = False
    
    def play_tetris(self):
        grid = Grid(rows=self.rows, columns=self.columns, params=self.params)
        tetris_piece = TetrisPiece.create_new_piece(rows=self.rows, columns=self.columns, grid=grid)
        buttons = Buttons(tetris_piece=tetris_piece, params=self.params)
        view = ft.Column(width=400,
                        controls=[grid, buttons],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.page.add(view)

        grid.color_pixels(tetris_piece=tetris_piece)
        while self.running:
            print(self.params['frame_rate_ms'])
            tetris_piece.move_piece(direction='down', params=self.params)
            can_be_played = grid.have_space()
            time.sleep(self.params['frame_rate_ms']/1000)
            if can_be_played==False:
                print('the end')
                self.play_tetris(self)
            


def main(page: ft.Page):
    page.title = "Tetris"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()
    page.add(Tetris())



if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
