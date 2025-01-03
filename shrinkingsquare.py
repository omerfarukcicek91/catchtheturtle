
import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")
turtle_instance.speed(1000)

def shringkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 10


shringkingSquare(150)
shringkingSquare(140)
shringkingSquare(130)
shringkingSquare(120)
shringkingSquare(110)
shringkingSquare(100)
shringkingSquare(90)
shringkingSquare(80)
shringkingSquare(70)
shringkingSquare(60)
shringkingSquare(50)
shringkingSquare(40)

turtle.done()