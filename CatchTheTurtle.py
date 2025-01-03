import threading
import time
import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle")
#ekran açılır ve 2 sn diğer satırlar beklenir.
time.sleep(2)


#turtles itself
turtle_instance = turtle.Turtle()
turtle_instance.hideturtle()
turtle_instance.penup()
turtle_instance.speed(2)
turtle_instance.shapesize(2)
turtle_instance.fillcolor("green")
turtle_instance.shape("turtle")

#information records

general_information = turtle.Turtle()
general_information.hideturtle()
general_information.penup()
general_information.goto(0,350)
general_information.write("LET'S START", align="center", font=("Arial", 24, "bold"))
time.sleep(1)
general_information.clear()
general_information.write("CATCH THE TURTLE", align="center", font=("Arial", 24, "bold"))

score_catch = turtle.Turtle()
score_catch.penup()
score_catch.hideturtle()
score_catch.goto(0, 250)
score_catch.clear()

countdown_turtle = turtle.Turtle()

countdown_turtle.penup()
countdown_turtle.hideturtle()
countdown_turtle.goto(0, 300)

def score():
    score_catch.write("Score:", align="center", font=("Arial", 24, "bold"))

def turtle_pen_up():
    turtle_instance.penup()
turtle_pen_up()

def random_movement():
    x = 0
    y = 0
    for _ in range(10):
        time.sleep(1)# 30 different position
        turtle_instance.hideturtle()
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        turtle_instance.setpos(x, y)
        turtle_instance.showturtle()
        print(x,y)
    return turtle_instance.setpos(x,y)


def countdown():
    for i in range(15, 0, -1):
        time.sleep(1)
        countdown_turtle.clear()
        countdown_turtle.write(f"{i}", align="center", font=("Arial", 24, "normal"))

    countdown_turtle.clear() # Geri sayım tamamlandığında yazıyı temizle
    turtle_instance.clear()
    countdown_turtle.write("GAME OVER!", align="center", font=("Arial", 24, "bold"))
    turtle.done()




mouse_click_coordinates = []
turtle_coordinates = []





def get_mouse_click_coordinates(x,y):
    mouse_click_coordinates.append((x,y))
    print (x,y)
turtle.onscreenclick(get_mouse_click_coordinates)


score_caught_count = turtle.Turtle()
score_caught_count.hideturtle()
score_caught_count.penup()
score_caught_count.goto(80, 250)
score_caught_count.write("0", align="center", font=("Arial", 24, "bold"))

final_score:int = 0
def is_turtle_clicked(x, y):
    # Turtle'ın pozisyonunu al
    global final_score
    turtle_pos = turtle_instance.position()


    # Tıklama koordinatını kontrol et
    if turtle_pos[0] - 20 <= x <= turtle_pos[0] + 20 and turtle_pos[1] - 20 <= y <= turtle_pos[1] + 20:
        final_score +=1
        score_caught_count.clear()
        score_caught_count.write(f"{final_score}", align="center", font=("Arial", 24, "bold"))
    else:
        print("missed")

turtle.onscreenclick(is_turtle_clicked)



'''
def score_count_comparison():
    i = 0
    for mouse_coords in mouse_click_coordinates:
        for turtle_coords in turtle_coordinates:
            if mouse_coords == turtle_coords:
                i = i+1
    score_caught_count.write(f"{i}", align="center", font=("Arial", 24, "bold"))
'''



#tüm satırların aynı anda başlaması için threads oluştururuz.

# Threadleri oluştur
countdown_thread = threading.Thread(target=countdown)
movement_thread = threading.Thread(target=random_movement)
score_thread = threading.Thread(target=score)
scorecaught_thread = threading.Thread(target=is_turtle_clicked)


# Threadleri başlat
countdown_thread.start()
movement_thread.start()
score_thread.start()
scorecaught_thread.start()



turtle.done()
#drawing_board.exitonclick()
