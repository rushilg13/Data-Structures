class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end
    
    def traverse(self):
        temp = self.head
        while temp.next:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print("End")
    
    def insert_end(self, value):
        if self.head==None:
            newNode=Node(value)
            self.head=newNode
            self.head.next=newNode
            self.end = newNode
            
        else:
            newNode=Node(value)
            self.end.next=newNode
            newNode.next=self.head
            self.end=newNode
    
    def insert_beg(self, value):
        newNode = Node(value)
        newNode.next=self.head
        self.head=newNode
        self.end.next=newNode
    
    def delete_end(self):
        temp = self.head
        while temp.next.next!=self.head:
            temp = temp.next
        temp.next = self.head
    
    def delete_beg(self):
        self.head = self.head.next
        self.end.next= self.head
    
    def size(self):
        temp = self.head
        count=0
        while temp.next:
            count+=1
            temp = temp.next
            if temp == self.head:
                break
        return count
    
    def insert_mid(self, ind, value):
        count=0
        temp=self.head
        if(MyList.size() < ind):
            print("List not Long Enough")
        else:
            while(count<ind-1):
                temp=temp.next
                count+=1
            newNode=Node(value)
            newNode.next = temp.next
            temp.next = newNode
    
    def delete_mid(self, ind):
        count = 0
        temp = self.head
        if(MyList.size()<ind):
            print("List Not Long Enough")
        else:
            while(count<ind-1):
                temp=temp.next
                count+=1
            temp.next=temp.next.next
    
    def exit_list(self):
        exit()



MyList = LinkedList()
MyList.insert_end(10)
MyList.insert_end(20)
MyList.insert_end(30)
MyList.traverse()
MyList.insert_beg(0)
MyList.insert_beg(-10)
MyList.traverse()
MyList.delete_beg()
MyList.delete_beg()
MyList.traverse()
MyList.delete_end()
MyList.traverse()
MyList.insert_end(30)
MyList.insert_end(40)
print("Size of list is:", MyList.size())
MyList.traverse()
MyList.insert_mid(2,99)
MyList.traverse()
MyList.delete_mid(1)
MyList.traverse()
MyList.exit_list()

