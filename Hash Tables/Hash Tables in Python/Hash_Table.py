class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def print_arr(self):
        print(self.arr)
    
    def get_key(self, value):
        key = value % self.MAX
        print(key)


hash = HashTable()
hash.print_arr()
