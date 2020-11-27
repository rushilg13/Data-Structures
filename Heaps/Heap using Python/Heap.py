class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def isEmpty(self):
        if(len(self.items==0)):
            return True
        else:
            return False

    def dequeue(self):
        if len(self.items)!=0:
            return self.items.pop()
    
    def peek(self):
        return self.items[-1].data
    
    def size(self):
        return len(self.items)
    
class Heap:
    def __init__(self, value):
        self.root = Node(value)
    
    def Levelorder(self, start, traversal):
        if start == None:
            return
        queue = Queue()
        arr=[]
        queue.enqueue(start)
        traversal = ""
        while queue.size() > 0:
            traversal+=str(queue.peek()) + "->"
            arr.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        print(traversal, end="End") 
    
    # def check_heap(self):
    #     arr = self.Levelorder(heap.root, "")
    #     arr.insert(0,None)
    #     for i in range(1,len(arr)):
    #         if(arr[int(i/2)] > arr[i*2] and arr[int(i/2)] > arr[(i*2)+1]):
    #             print("heap")
    #         else:
    #             print("no")
    #     print(arr)



    


heap = Heap(100)
heap.root.left = Node(40)
heap.root.left.left = Node(30)
heap.root.left.right = Node(20)
heap.root.right = Node(50)
heap.root.right.left = Node(40)
heap.root.right.right = Node(30)
heap.Levelorder(heap.root, "")
'''
            100
           /    \
          40     50
        /   \   /  \
       30   20 40   30     

'''


