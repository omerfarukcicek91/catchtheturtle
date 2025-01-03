import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("Black")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("white")
turtle_instance.speed(100)

turtle_colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(50):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(5 * i)
    turtle_instance.circle(-5 * i)
    turtle_instance.left(i)


turtle.mainloop()
#turtle.done()