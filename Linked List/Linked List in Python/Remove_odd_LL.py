class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def insert(self, value):
        if self.start == None:
            self.start = Node(value)
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = Node(value)
    
    def display(self):
        if self.start == None:
            print("List Empty!")
        else:
            temp = self.start
            while temp.next != None:
                print(temp.value, end = "->")
                temp = temp.next
            print("End")
            
            t
