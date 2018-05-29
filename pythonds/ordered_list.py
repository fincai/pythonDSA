class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    
class OrderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        while current != None:
            if current.getData() > data:
                return False
            elif current.getData() == data:
                return True
            else:
                current = current.getNext()
        return False

    def add(self, data):
        current = self.head
        previous = None
        while current != None:
            if current.getData() < data:
                previous = current
                current = current.getNext()
            else:
                break
        newnode = Node(data)
        if previous == None:
            self.head = newnode
            newnode.setNext(current)
        else:
            previous.setNext(newnode)
            newnode.setNext(current)
