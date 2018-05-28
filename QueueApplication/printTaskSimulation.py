import random
import sys
sys.path.append("..")
from pythonds.queue import Queue

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        return self.currentTask != None

    def startnext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60  / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
        
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp
        
def newPrintTask():
    return random.randrange(1, 181) == 180

def simulation(numSeconds, pagesPerMin):
    labprinter  = Printer(pagesPerMin)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            #print("new")
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startnext(nexttask)

        labprinter.tick()
            
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Waiting Time: %6.2f secs. %3d tasks remaining." % \
                                (averageWait, printQueue.size()))
    

for i in range(10):
    simulation(3600, 10)
