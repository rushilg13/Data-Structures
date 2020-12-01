class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def insert(self, value):
        if self.start == None:
            self.start.next = Node(value)
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(value)
    