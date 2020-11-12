queue=[]
choice=0
def enqueue():
    num = int(input())
    queue.append(num)

def dequeue():
    del queue[0]

def display():
    # stack.reverse()
    print(queue)

while(choice!=5):
    print("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\nYour choice:")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        exit()