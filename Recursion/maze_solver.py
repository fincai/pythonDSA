import turtle

OBSTACLE = '+'
DEAD_END = '-'
TRIED = '.'
PART_OF_PATH = '0'

class Maze:
    def __init__(self, mazefile):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazef = open(mazefile, 'r')
        for line in mazef:
            rowlist = []
            col = 0
            for ch in line:
                rowlist.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazelist.append(rowlist)
            columnsInMaze = len(rowlist)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2  
        self.yTranslate = rowsInMaze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.window = turtle.Screen()
        self.window.setworldcoordinates(-(columnsInMaze-1)/2-.5,  # lower left
                                        -(rowsInMaze-1)/2-.5,
                                        (columnsInMaze-1)/2+.5,   # upper right
                                        (rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.window.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE: 
                    self.drawCenteredBox(x + self.xTranslate,
                                         -y + self.yTranslate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.window.update()
        self.window.tracer(1)


    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x-0.5, y-0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)  # north
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
    def dropBreadcrumb(self, color):
        self.t.dot(20, color)


    def moveTurtle(self, x, y):
        self.t.penup()
        self.t.setheading(self.t.towards(x+self.xTranslate,
                                         -y+self.yTranslate))
        self.t.goto(x+self.xTranslate, -y+self.yTranslate)

    def updatePosition(self, row, col, val=None):
        self.moveTurtle(col, row)
        if val:
            self.mazelist[row][col] = val
            if val == TRIED:
                color = 'black'
            elif val == PART_OF_PATH:
                color = 'green'
            elif val == DEAD_END:
                color = 'red'
            else:
                color = None
            if color:
                self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (row == 0 or  
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1)

    def __getitem__(self, idx):  # overload [] operator
        return self.mazelist[idx]

def searchFrom(maze, startRow, startCol):
    maze.updatePosition(startRow, startCol) # move turtle(cursor) to this position
    if maze[startRow][startCol] == OBSTACLE:
        return False
    if maze[startRow][startCol] == TRIED:
        return False
    if maze[startRow][startCol] == DEAD_END:
        return False
    if maze.isExit(startRow, startCol):
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
        return True

    maze.updatePosition(startRow, startCol, TRIED)
    found = searchFrom(maze, startRow-1, startCol) or \
            searchFrom(maze, startRow+1, startCol) or \
            searchFrom(maze, startRow, startCol-1) or \
            searchFrom(maze, startRow, startCol+1) 
    if found:
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startCol, DEAD_END)
    return found
            
            
    
        
myMaze = Maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow, myMaze.startCol)
searchFrom(myMaze, myMaze.startRow, myMaze.startCol)

myMaze.window.exitonclick()
