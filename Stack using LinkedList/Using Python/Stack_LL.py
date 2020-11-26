class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_LL:
    def __init__(self):
        self.start = None

    def insert(self, value):
        if self.start == None:
            self.start = Node(value)   
        else:
            temp = self.start
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(value)
    


SLL = Stack_LL()
SLL.insert(10)
SLL.insert(20)
SLL.insert(30)     