import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("CATCH THE TURTLE")
FONT = ('Arial', 30, 'normal')
#her bir kalem için bir turtle oluşturacağız.
score = 0
game_over = False
#turtle list
turtle_list = []
grid_size = 15
#score turtle
score_turtle = turtle.Turtle()

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10]
#countdown turtle
countdown_turtle = turtle.Turtle()

#score turtle içeriğini yazdıktan sonra çağırabilmek için bir fonksiyona alacağız. fonksiyon bazlı olarak çalışmamız lazım. Karışıklığı önlemek adına.

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("dark blue")

    top_height = screen.window_height()/2
    y = top_height * 0.85
    #score_turtle.setposition(0,300) -> örnek 1
    #score_turtle.goto(x=0, y=300) -> örnek 2
    #score_turtle.position() -> örnek 3
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0", move= False, align="center",font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score +=1
        score_turtle.clear()
        print(x, y)
        score_turtle.write(arg="Score: {}".format(score), move= False, align= "center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.speed(10)
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

def turtle_coordinates():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#1 adeti gösterme

#kendi içerisinde bir fonksiyon çalışıyorsa, recursive bir fonksiyonsa, bir exit point olması lazım if fonk içerisinde.
def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly, 1000)

'''
def countdown():
    import time
    number = 10
    while number > 0:
        print(number)
        time.sleep(1)
        number -= 1

'''

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height()/2
    y = top_height * 0.85
    countdown_turtle.setposition(0,y - 50)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()

        countdown_turtle.write(arg="Time: {}".format(time), move= False, align="center",font=FONT)
        screen.ontimer(lambda: countdown(time -1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="GAME OVER!", move= False, align="center",font=FONT)

def start_game_up():

    turtle.tracer(0)
    turtle_coordinates()
    setup_score_turtle()
    hide_turtles()
    show_turtle_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()

