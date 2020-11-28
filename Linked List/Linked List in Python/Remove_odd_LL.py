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
    
    def remove_odd(self):
        if self.start==None:
            print("List Empty!")
        else:
            self.start = self.start.next
            temp = self.start
            while(temp.next != None):
                temp.next = temp.next.next
                temp = temp.next




LL = LinkedList()
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.insert(40)
LL.insert(50)
LL.insert(60)
LL.insert(70)
LL.insert(80)
LL.insert(90)
LL.insert(100)

LL.display()
print("Lenth of LinkedList is:", LL.get_len())
LL.remove_odd()
LL.display()
print("Lenth of LinkedList is:", LL.get_len())

            
            
