class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_LL:
    def __init__(self):
        self.start = None
    
    def enqueue(self, value):
        if self.start == None:
            self.start = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.start
            self.start = newNode
    
    def display(self):
        temp = self.start
        while(temp!=None):
            print(temp.data, end="->")
            temp = temp.next
        print("Front")

QLL = Queue_LL()
QLL.enqueue(10)
QLL.enqueue(20)
QLL.enqueue(30)
QLL.display()
