class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
    
    def insert_end(self, value):
        newNode = Node(value)
        if self.head==None:
            newNode.prev=None
            self.head = newNode
            self.head.next = None
        else:
            temp = self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next = newNode
            newNode.prev = temp
            newNode.next = None
    
    def insert_start(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        newNode.prev = None

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("End")
    
    def size(self):
        temp = self.head
        count = 0
        while temp != None:
            count+=1
            temp = temp.next
        return(count)

    def insert_mid(self, ind, value):
        if (ind > MyList.size()):
            print("List is not long enough")
        else:
            count = 0
            temp = self.head
            while count<ind-1:
                count+=1
                temp = temp.next
            newNode = Node(value)
            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next=newNode
    
    def delete_start(self):
        self.head = self.head.next
        self.head.prev = None
    
    def delete_end(self):
        temp = self.head
        while(temp.next!=None):
            temp = temp.next
        temp.prev.next = None

    def delete_mid(self, ind):
        if (ind > MyList.size()):
            print("List is not long enough")
        else:
            count = 0
            temp = self.head
            while count<ind-1:
                count+=1
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp
    
    def exit_DLL(self):
        exit()
   
    



MyList = DLL()
MyList.insert_end(10)
MyList.insert_end(20)
MyList.insert_end(30)
MyList.display()
MyList.insert_start(0)
MyList.insert_start(-10)
MyList.display()
print("Size of linkedList is:",MyList.size())
MyList.insert_mid(4,99)
MyList.display()
MyList.delete_start()
MyList.display()
MyList.delete_end()
MyList.display()
MyList.delete_mid(2)
MyList.display()
MyList.exit_DLL()




