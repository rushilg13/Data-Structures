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
    
    def dequeue(self):
        if self.start == None:
            print("Queue is Empty")
        else:
            temp = self.start
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None   

    def peek(self):
        if self.start == None:
            print("Queue is Empty")
        else:
            temp = self.start
            while(temp.next!=None):
                temp = temp.next
            print(temp.data)

    def is_empty(self):
        if self.start == None:
            print("Queue is Empty")
            return
        else:
            print("Queue is Not Empty!")

QLL = Queue_LL()
QLL.enqueue(10)
QLL.enqueue(20)
QLL.enqueue(30)
QLL.display()
QLL.dequeue()
QLL.display()
QLL.peek()
QLL.is_empty()