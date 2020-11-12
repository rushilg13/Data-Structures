stack=[]
top=-1
choice=0
def push(top):
    top=top+1
    num = int(input())
    stack.append(num)

def pop(top):
    top=top-1
    stack.pop()

def display():
    # stack.reverse()
    print(stack)

def peek(top):
    print(stack[top])

while(choice!=5):
    print("\n1.Push\n2.Pop\n3.Display\n4.Peek\n5.Exit\nYour choice:")
    choice=int(input())
    if choice==1:
        push(top)
    elif choice==2:
        pop(top)
    elif choice==3:
        display()
    elif choice==4:
        peek(top)
    elif choice==1:
        exit()



    