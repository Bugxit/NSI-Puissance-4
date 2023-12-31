import turtle as tu
from tkinter import messagebox
import itertools as tool
import time as ti
import os

size = 1920/1920

#Paramétrage de turtle (Force fullscreen)
tu.hideturtle()
tu.Screen().setup(1920/size,1080/size)
tu.Screen().getcanvas().winfo_toplevel().overrideredirect(1)
tu.Screen().tracer(0)

class Piece(tu.Turtle):

    def __init__(self, coords, color):
        super().__init__(visible = False)
        self.coords = coords
        self.color = color
        self.pause = False

    def draw_dot(self, temp_coords, current_color):
        self.color = current_color
        self.goto(150*(temp_coords[0]-3)/size, temp_coords[1])
        self.clear()
        self.dot(100/size, f'{self.color}')
        tu.Screen().update()

    def draw_piece(self):
        global drop_count, current_color
        self.goto(150*(self.coords[0]-3)/size, (self.coords[1]*150-475)/size)
        self.down()
        self.clear()
        self.dot(100/size, f'{self.color}')
        if self == choose_piece and drop_count % 2 == 0:
            self.dot(75/size, 'yellow')
        elif self == choose_piece:
            self.dot(75/size, 'red')

    #Function in charge of the animation of the piece falling
    def drop_piece(self):
        global pause, drop_count, current_color
        if pause == False and self.coords[0] != -1 and height_rows[self.coords[0]] != 6:
            drop_count += 1
            pause = True
            board[height_rows[self.coords[0]]][self.coords[0]].draw_piece()
            if drop_count % 2 == 0:
                current_color = 'red'
            else:
                current_color = 'yellow'
            choose_piece.draw_piece()
            for y in range(int(round((150*(6-height_rows[self.coords[0]])+25)/size))):
                board[height_rows[self.coords[0]]][self.coords[0]].draw_dot((self.coords[0], (450-y)), current_color)
            board[height_rows[self.coords[0]]][self.coords[0]].color = current_color
            board[height_rows[self.coords[0]]][self.coords[0]].draw_piece()
            height_rows[self.coords[0]] += 1
            self.check_victory()
            pause = False

    def check_victory(self):
        #Checking if there if 4 pieces aligned horizontaly
        for x_test, y_test in tool.product(range(4), range(6)):
            h_test = 0
            while board[y_test][x_test+h_test].color == board[y_test][x_test].color and board[y_test][x_test].color != 'white':
                if h_test == 3:
                    tu.bye()
                    os.system('cls')
                    print(f'{board[y_test][x_test].color.upper()} has won')
                    ti.sleep(2)
                    exit()
                else:
                    h_test += 1
        #Checking if there is 4 pieces aligned verticaly
        for x_test, y_test in tool.product(range(7), range(3)):
            v_test = 0
            while board[y_test+v_test][x_test].color == board[y_test][x_test].color and board[y_test][x_test].color != 'white':
                if v_test == 3:
                    tu.bye()
                    os.system('cls')
                    print(f'{board[y_test][x_test].color.upper()} has won')
                    ti.sleep(2)
                    exit()
                else:
                    v_test += 1
        #Checking if there is 4 pieces aligned diagonally 
        for x_test, y_test in tool.product(range(4),range(3)):
            d0_test = 0
            while board[y_test+d0_test][x_test+d0_test].color == board[y_test][x_test].color and board[y_test][x_test].color != 'white':
                if d0_test == 3:
                    tu.bye()
                    os.system('cls')
                    print(f'{board[y_test][x_test].color.upper()} has won')
                    ti.sleep(2)
                    exit()
                else:
                    d0_test += 1  
        #Checking if there is 4 pieces aligned diagonally 
        for x_test, y_test in tool.product(range(3,7), range(3)):
            d1_test = 0
            while board[y_test+d1_test][x_test-d1_test].color == board[y_test][x_test].color and board[y_test][x_test].color != 'white':
                if d1_test == 3:
                    tu.bye()
                    os.system('cls')
                    print(f'{board[y_test][x_test].color.upper()} has won')
                    ti.sleep(2)
                    exit()
                else:
                    d1_test += 1
        os.system('cls')       

    #Mooves the piece to the right
    def right(self):
        if pause == False and self.coords[0] in [-1, 0, 1, 2, 3, 4]:
            self.coords[0] += 1
            self.draw_piece()
            
    #Mooves the piece to the left
    def left(self):
        if pause == False and self.coords[0] in [1, 2, 3, 4, 5]:
            self.coords[0] += -1
            self.draw_piece()
            
#Function that draw the outerlines of the board
def draw_board():
    for i in [-1,1]:
        tu.up()
        tu.goto((i*525-(i+1)*75)/size, -540/size)
        tu.seth(90)
        tu.down()
        tu.forward(900/size)
#Setting up the board and the variables/Lists
draw_board()
board = [[Piece([x,y], 'white') for x in range(7)] for y in range(6)]
height_rows = [0 for x in range(7)]
current_color = 'red'
choose_piece = Piece([-1, 6], 'black')
game_end = False
drop_count = 0

choose_piece.draw_piece()
pause = False

while game_end == False and pause == False:
    tu.listen()
    tu.onkeypress(choose_piece.drop_piece, 'Down')
    tu.onkeypress(choose_piece.right, 'Right')
    tu.onkeypress(choose_piece.left, 'Left')
    tu.Screen().update()
