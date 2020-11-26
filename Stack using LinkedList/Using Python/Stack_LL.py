class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_LL:
    def __init__(self):
        self.start = None

    def push(self, value):
        if self.start == None:
            self.start = Node(value)   
        else:
            temp = self.start
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(value)
    
    def display(self):
        if self.start==None:
            print("Stack is Empty!")
        else:
            temp = self.start
            while(temp!=None):
                print(temp.data, end="->")
                temp = temp.next
            print("Top")

    def pop(self):
        if self.start == None:
            print("Stack is Empty!")
        else:
            temp = self.start
            while(temp.next.next!=None):
                temp = temp.next
            temp.next = None     


SLL = Stack_LL()
SLL.push(10)
SLL.push(20)
SLL.push(30)
SLL.push(40)     
SLL.display()
SLL.pop()
SLL.display()