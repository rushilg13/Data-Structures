class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def print_arr(self):
        print(self.arr)
    
    def get_key(self, value):
        key = value % self.MAX
        return key
    
    def add(self, key, value):
        ind = self.get_key(key)
        self.arr[ind] = value 
    
    def count(self):
        count = 0
        for i in self.arr:
            if(i!=None):
                count+=1
        print("Currently there are", count, "entries in Hash table")

    def delete(self, key):
        ind = self.get_key(key)
        self.arr[ind] = None



hash = HashTable()
hash.add(617,"Austin")
hash.add(411,"Moon")
hash.add(132,"Gerald")
hash.add(243,"Mathew")
hash.add(218,"Andrew")
hash.add(959,"Kylie")
hash.add(0,"Timberlake")
hash.add(624,"Justin")
hash.add(95,"Sarah")
hash.add(916,"Miley")

hash.print_arr()

hash.count()

hash.delete(216)

hash.count()
