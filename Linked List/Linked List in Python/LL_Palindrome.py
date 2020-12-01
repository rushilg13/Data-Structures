class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def insert(self, value):
        if self.start == None:
            self.start = Node(value)
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(value)
        
    def display(self):
        if self.start == None:
            print("LinkedList is empty")
        else:
            temp = self.start
            while(temp != None):
                print(temp.value, end="->")
                temp = temp.next
            print("End")
    
    def check_palindrome(self):
        s1 = s2 = ""
        if self.start == None:
            print("LinkedList is empty")
        else:
            temp = self.start
            while(temp != None):
                s1 = s1 + temp.value
                temp = temp.next
            print(s1)


LL = LinkedList()
LL.insert("a")
LL.insert("b")
LL.insert("c")
LL.display()
LL.check_palindrome()