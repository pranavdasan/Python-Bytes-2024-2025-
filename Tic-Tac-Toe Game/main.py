import turtle

screen = turtle.Screen()

# Title of the screen
screen.title("Tic-Tac-Toe")

# Setup the screen size
screen.setup(width = 600, height = 600)

# The drawing tool
t = turtle.Turtle()

t.hideturtle() # Hides the turtle

t.speed(0) # So the drawing is instant


def draw_grid():
    t.pensize(5) # Sets the pensize to be 5 pixels

    # Verticle lines
    for x in [-100, 100]:
        t.penup()
        t.goto(x, 300)
        t.pendown()
        t.goto(x, -300)
    
    # Horizontal Lines
    for y in [-100, 100]:
        t.penup()
        t.goto(300, y)
        t.pendown()
        t.goto(-300, y)

def draw_x(x, y):
    size = 50 # Size of the X
    t.penup()

    # Draw the first diagonal line
    t.goto(x-size, y-size) # Moves turtle to starting posistion
    t.pendown()
    t.pensize(5)
    t.pencolor("red")
    t.goto(x+size, y+size)

    t.penup()

    # Draw the second diagonal line
    t.goto(x-size,y + size) # Moves turtle to starting posistion
    t.pendown()
    t.goto(x+size, y - size)

def draw_circle(x, y):
    t.penup()

    # Moves the turtle to the center of the circle
    t.goto(x, y - 50)

    t.pendown()

    t.pencolor("blue")

    t.circle(50) 
    
    

def draw_piece(x,y):
    # Tells Python to access the variable outside the function
    global player_x_turn

    # Snaps the coordinates to the grid
    if x < -100:
        grid_x = -200
    elif x > 100:
        grid_x = 200
    else: 
        grid_x = 0

    if y < -100:
        grid_y = -200
    elif y > 100:
        grid_y = 200
    else:
        grid_y = 0

    if player_x_turn:
        draw_x(grid_x, grid_y)
        player_x_turn = False
    else:
        draw_circle(grid_x, grid_y)
        player_x_turn = True

def clear_game():
    t.clear()
    draw_grid()


draw_grid()

player_x_turn = True

screen.onclick(draw_piece)

# Check whether r key is being pressed
screen.onkey(clear_game, "r")

screen.listen() # Listen for any key presses

screen.mainloop() # Keeps the screen always on