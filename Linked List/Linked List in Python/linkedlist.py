# Linked List in Python

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None

    def view(self):
        if(self.start==None):
            print("Empty list\n")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data, end=" ")
                temp=temp.next
            print()
    
    def DeleteFromStart(self):
        if self.start==None:
            print("List is empty. Nothing to delete!\n")
        else:
            print("Deleted value is:", self.start.data)
            self.start=self.start.next

    def InsertInEnd(self,value):
        newNode=node(value)
        if(self.start==None):
            self.start=newNode
        else:
            temp=self.start
            while(temp.next != None):
                temp=temp.next
            temp.next=newNode

# Driver Menu
ch=0
myList=LinkedList()
while(ch!=4):
    print("1. Insert at End\n2. Delete from Start\n3. Display\n4. Exit")
    ch=int(input())
    if(ch==1):
        print("Enter Value to insert:")
        n=int(input())
        myList.InsertInEnd(n)
    elif(ch==2):
        myList.DeleteFromStart()
    elif(ch==3):
        myList.view()
    elif(ch==4):
        exit()        

