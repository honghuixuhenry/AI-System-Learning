class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash(self, key):
        return key % self.size

    def insert(self,key):
        index = self.hash(key)
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)
        return self.table[index]

    def delete(self, key):
        index = self.hash(key)
        self.table[index] = None

    def display(self):
        print(self.table)

hash_table = HashTable()
hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(35)

print(hash_table.search(15))

hash_table.delete(15)

hash_table.display()


    

    