class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def print_arr(self):
        print(self.arr)
    
    def get_key(self, value):
        key = value % self.MAX
        return key
    
    def add(self, key, value):
        ind = self.get_key(key)
        self.arr[ind] = value 


hash = HashTable()
hash.add(21,"Austin")
hash.print_arr()