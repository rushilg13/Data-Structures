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
            while temp != None:
                print(temp.value, end = "->")
                temp = temp.next
            print("End")
    
    def get_len(self):
        if self.start==None:
            print("List Empty!")
        else:
            count=0
            temp = self.start
            while temp != None:
                count+=1
                temp = temp.next
            return (count)


LL1 = LinkedList()
LL1.insert(10)
LL1.insert(20)
LL1.insert(30)
LL1.insert(40)
LL1.insert(50)
LL1.insert(60)
LL1.insert(70)
LL1.insert(80)
LL1.insert(90)
LL1.insert(100)

LL1.display()

LL2 = LinkedList()
LL2.insert(1)
LL2.insert(2)
LL2.insert(3)
LL2.insert(4)
LL2.insert(5)
LL2.insert(6)
LL2.insert(7)
LL2.insert(8)
LL2.insert(9)
LL2.insert(11)

LL2.display()
                        

