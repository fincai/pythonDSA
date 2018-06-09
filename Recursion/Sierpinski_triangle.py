import turtle

colormap = ['#d47aa5', '#f7e72c', 'white', '#13913a', '#ca1b26', '#21246b', 'violet']

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.setpos(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.setpos(points[1][0], points[1][1])
    myTurtle.setpos(points[2][0], points[2][1])
    myTurtle.setpos(points[0][0], points[0][1])
    myTurtle.end_fill()

def getmid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(points, degree, myTurtle):
    drawTriangle(points, colormap[degree], myTurtle) 
    if degree > 0:
        sierpinski([points[0], getmid(points[0], points[1]),
                               getmid(points[0], points[2])],
                    degree-1, myTurtle)
        sierpinski([points[1], getmid(points[1], points[0]),
                               getmid(points[1], points[2])],
                    degree-1, myTurtle)
        sierpinski([points[2], getmid(points[2], points[1]),
                               getmid(points[2], points[0])],
                    degree-1, myTurtle)
        

myTurtle = turtle.Turtle()
myWindow = turtle.Screen()
myPoints = [(-400, -200), (0, 400), (400, -200)]
sierpinski(myPoints, 5, myTurtle)
myWindow.exitonclick()
