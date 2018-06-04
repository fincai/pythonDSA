import turtle

myTurtle = turtle.Turtle()
myWindow = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)  # turn right 90 degree
        drawSpiral(myTurtle, lineLen-5)

drawSpiral(myTurtle, 100)
myWindow.exitonclick()

