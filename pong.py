#Author: Emmanuel Makau
#Date: 10/12/2022
#Purpose: Pong Game
#Kasuti Kreations

#Import
from cs1lib import*

#Paddles (l-left, r-right)
l = 20
h = 80
xl = 0
yl = 0
xr = 380
yr = 320

#Keys
kpress = False
mpress = False
apress = False
zpress = False
qpress = False
space_press = False
game_progress = True

#Ball
R = 10
x_ball = 200
y_ball = 200

#Velocity
x_bv = 5
y_bv = 5

#Background
def background():
    set_clear_color(.25, .25, .25) #Dark grey

#Paddles
def paddles():
    set_stroke_color(0, 1, 0) #Green
    set_fill_color(0, 1, 0)
    draw_rectangle(xl, yl, l, h) #left
    draw_rectangle(xr, yr, l, h) #right

#Ball
def ball():
    set_stroke_color(1, 1, 0) #Yellow
    set_fill_color(1, 1, 0)
    draw_circle(x_ball, y_ball, R)

#Velocity
def ball_velocity():
    global x_ball, y_ball
    x_ball += x_bv
    y_ball += y_bv

#Collision with pedals
def collision_with_paddles():
    global x_bv

    #left paddle
    if 20 < x_ball < 30 and yl < y_ball < (yl + h):
        x_bv = - x_bv
    #right paddle
    if 370 < x_ball < 380 and yr < y_ball < (yr + h):
        x_bv = -x_bv

#Collision with walls
def collision_with_walls():
    global y_bv

    #Upper wall
    if y_ball < 10:
        y_bv = -y_bv
    #Lower wall
    if y_ball > 390:
        y_bv = -y_bv

#Collision with sidewalls
def collision_with_sidewalls():
    global game_progress
    if 0 < x_ball < 10 or 390 < x_ball < 400:
        game_progress = False

#Key pressing
def k_press(key):
    global apress, zpress, kpress, mpress, qpress, space_press, game_progress, xl, yl, xr, yr, x_ball, y_ball

    if key == "a": #left paddle up
        apress = True
    if key == "z": #left paddle down
        zpress = True
    if key == "k": #right paddle up
        kpress = True
    if key == "m": #right paddle down
        mpress = True
    if key == "q": #quits game
        qpress = True
    if key == " ": #restarts game
        space_press = True

    # Moving the paddles
    if apress == True and yl > 0:
        yl -= 10
    if zpress == True and yl < 320:
        yl += 10
    if kpress == True and yr > 0:
        yr -= 10
    if mpress == True and yr < 320:
        yr += 10

    #Quiting the game
    if qpress == True:
        cs1_quit()

    #Restart the game
    if space_press == True:
        game_progress = True
        x_ball = 200
        y_ball = 200
        xl = 0
        yl = 0
        xr = 380
        yr = 320

#Key releasing
def k_release(key):
    global apress, zpress, kpress, mpress, qpress, space_press

    if key == "a": #left paddle up
        apress = False
    if key == "z": #left paddle down
        zpress = False
    if key == "k": #right paddle up
        kpress = False
    if key == "m": #right paddle down
        mpress = False
    if key == "q": #quits game
        qpress = False
    if key == " ": #restarts game
        space_press = False

#Main function
def pong():
    global game_progress, x_ball, y_ball

    if game_progress: #True
        clear()
        background()
        paddles()
        ball()
        ball_velocity()
        collision_with_paddles()
        collision_with_walls()
        collision_with_sidewalls()
    else:
        set_stroke_color(1, 1, 1)
        draw_text("GAME OVER", 150, 200)
        x_ball = 200
        y_ball = 200

start_graphics(pong, key_press=k_press, key_release=k_release)