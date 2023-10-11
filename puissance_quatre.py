import turtle as tu
import itertools as tool

tu.hideturtle()
tu.Screen().setup(1920,1080)
canvas = tu.Screen().getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
tu.Screen().tracer(0)

class Piece(tu.Turtle):
    
    def __init__(self, coords, color):
        super().__init__(visible = False)  
        self.coords = coords
        self.color = color
    
    def clear_piece(self):
        self.clear()
        
    def draw_dot(self):
        self.up()
        self.goto(150*(self.coords[0]-3), self.coords[1]*150-475)
        self.down()
        self.dot(100, f'{self.color}')
        
    def drop(self):
        global drop
        drop = True
        
    def right(self):
        self.coords[0] += 1
        self.clear_piece()
        
    def left(self):
        self.coords[0] += -1
        self.clear_piece()
        
board = [[(Piece([x, y], 'red')) for x in range(7)] for y in range(6)]
choose_piece = Piece([-1, 6], 'black')

for x, y in tool.product(range(7), range(6)):
    board[y][x].draw_dot()
drop = False

while drop == False:
    tu.listen()
    tu.onkeypress(choose_piece.drop,'Down')
    tu.onkeypress(choose_piece.right, 'Right')
    tu.onkeypress(choose_piece.left, 'Left')
    choose_piece.draw_dot()
    tu.Screen().update()