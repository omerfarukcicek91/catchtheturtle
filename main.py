import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#a97142") # bg yi yeşil yaptı. green tanımlı olduğu için kabul ediyor.
drawing_board.title("Python Turtle")

#Square
'''
turtle_square = turtle.Turtle()
turtle_square.speed(5)
turtle_square.forward(300)
turtle_square.left(90)
turtle_square.forward(300)
turtle_square.left(90)
turtle_square.forward(300)
turtle_square.left(90)
turtle_square.forward(300)
'''


'''
for i in range(4):
    turtle_instance2 = turtle.Turtle()
    turtle_instance2.left(135)
    turtle_instance2.forward(100)
    turtle_instance2.clear()
    turtle_instance2.clearstamps()
'''

#star
'''
turtle_star = turtle.Turtle()
turtle_star.left(36)
turtle_star.forward(60)
turtle_star.left(108)
turtle_star.forward(60)
turtle_star.right(36)
turtle_star.forward(60)
turtle_star.left(108)
turtle_star.forward(60)
turtle_star.right(36)
turtle_star.forward(60)
turtle_star.left(108)
turtle_star.forward(60)
turtle_star.right(36)
turtle_star.forward(60)
turtle_star.left(108)
turtle_star.forward(60)
turtle_star.right(36)
turtle_star.forward(60)
turtle_star.left(108)
turtle_star.forward(60)
'''


#star2
'''
turtle_star2 = turtle.Turtle()
for i in range(5):
    turtle_star2.right(144)
    turtle_star2.forward(100)
'''

#polygon
'''
turtle_polygon = turtle.Turtle()
num_sides = 9
angle = 360.0 / num_sides*2
side_length = 100

for i in range(num_sides):
    turtle_polygon.right(angle)
    turtle_polygon.forward(side_length)
'''



turtle.done()




