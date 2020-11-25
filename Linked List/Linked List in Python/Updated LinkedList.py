class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def insert_end(self,value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    
    def view(self):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            while(temp != None):
                print(temp.data, end='->')
                temp = temp.next
            print("End")
    
    def delete_start(self):
        if self.start == None:
            print("Nothing to delete!")
        else:
            self.start = self.start.next
    
    def insert_ind(self, ind, value):
        count= 0
        temp = self.start
        while temp != None:
            count += 1
            print(count)
            temp = temp.next
        if ind > count+1:
            print("List Not Long enough")
        else:
            count=0
            temp = self.start
            while count!=ind-1:
                count+=1
                temp = temp.next
            newNode = Node(value)
            newNode.next = temp.next
            temp.next = newNode
    
    def insert_start(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode
    
    def delete_end(self):
        temp = self.start
        while(temp.next.next):
            temp = temp.next
        temp.next=None

    def delete_ind(self, ind):
        count=-1
        temp = self.start
        while(temp!=None):
            count+=1
            temp=temp.next
        if(ind>count):
            print("Index not in range!")
        else:
            count=-1
            temp=self.start
            while(count!=ind-2):
                temp=temp.next
                count+=1
            temp.next=temp.next.next
    
    def search(self, value):
        temp = self.start
        ind=-1
        while(temp!=None):
            ind+=1
            if(temp.data==value):
                flag=1
                break
            else:
                flag=0
                temp=temp.next
        if(flag==1):
            print("Value found at index", ind)
        else:
            print("Value Not found!")
            

    
print("Following are the Operations implemented so far:")
print("1. Insert at End\n2. Insert at an index\n3. Insert at Start\n4. Delete at End\n5. Delete at an index\n6. Delete at Start\n7. Display\n8. Search\n9. Exit")

Mylist = LinkedList()
Mylist.insert_end(10)
Mylist.insert_end(20)
Mylist.insert_end(30)
Mylist.insert_end(40)
Mylist.insert_end(50)
Mylist.view()
Mylist.delete_end()
Mylist.view()
Mylist.delete_ind(3)
Mylist.view()
Mylist.search(30)
