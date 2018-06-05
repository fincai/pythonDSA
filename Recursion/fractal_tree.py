import turtle
import random

def tree(branchLen, t):
    if branchLen > 5:
        if branchLen < 20:
            t.pencolor("green")
        t.forward(branchLen)
        rangle = random.randrange(15, 45)
        t.right(rangle)
        tree(branchLen-15, t)
        t.left(rangle*2)
        tree(branchLen-15, t)
        t.right(rangle)            # restore the direction in upper call
        t.backward(branchLen)
        t.pencolor("brown")
    
    

def main():
    t = turtle.Turtle()
    myWindow = turtle.Screen()
    t.left(90)
    t.penup()
    t.backward(250)
    t.pendown()
    #t.color("green")
    t.pensize(10)
    tree(120, t)
    myWindow.exitonclick()

main()
