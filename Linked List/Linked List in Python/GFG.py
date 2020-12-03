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
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(value)
    
    def display(self):
        if self.start == None:
            print("LinkedList is Empty!")
        else:
            temp = self.start
            while(temp != None):
                print(temp.value, end="->")
                temp = temp.next
            print("End")
    # https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
    # APPROACH 1, Count size, then go halfway
    def size(self):
        count = 0
        if self.start == None:
            print("LinkedList is Empty!")
            return 0
        else:
            temp = self.start
            while(temp != None):
                count+=1
                temp = temp.next
            return count
    
    def Middle_1(self):
        count = LL.size()
        if count == 0:
            print("No elements in list!")
        if count%2 == 0:
            counter = 0
            temp = self.start
            while(temp.next != None and counter != (count/2)-1):
                counter+=1
                temp = temp.next
            temp.next = temp.next.next

        if count%2 != 0:
            counter = 0
            temp = self.start
            while(temp.next != None and counter != int(count/2)-1):
                counter+=1
                temp = temp.next
            temp.next = temp.next.next
    
    # APPROACH 2, Traverse linked list using two pointers. Move one pointer by one and the other pointers by two. When the fast pointer reaches the end slow pointer will reach the middle of the linked list.

    def Middle_2(self):
        if self.start == None:
            print("LinkedList is Empty!")
        else:
            behind = self.start
            ahead = self.start
            while(ahead != None):
                behind = behind.next
                ahead = ahead.next.next
            print(behind.value)   

LL = LinkedList()
LL.display()
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.insert(40)
LL.display()
print(LL.size())
LL.Middle_2()
LL.display()
print(LL.size())
