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

    def setNext(self, nextNode):
        self.next = nextNode


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, newdata):
        temp = Node(newdata)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        while current != None:
            if current.getData() == data:
                return True
            else:
                current = current.getNext()
        return False

    # assume the data is in the list
    def remove(self, data):
        previous = None
        current = self.head
        while True:
            if current.getData() == data:
                break
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
