import constants
import util

class CuckooHashing:
    def __init__(self):
        self.size = constants.HASH_TABLE_SIZE
        self.hash_table1 = [-1] * self.size
        self.hash_table2 = [-1] * self.size
        self.unsuccessful_insertion_count = 0

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return (key // self.size) % self.size

    def insert(self, key, hash_table1, hash_table2):
        if self.search(key):
            return True
        
        for _ in range(self.size):
            hash_1, hash_2 = self.hash1(key), self.hash2(key)
            if hash_table1[hash_1] == -1:
                hash_table1[hash_1] = key
                return True
            key, hash_table1[hash_1] = hash_table1[hash_1], key
            if hash_table2[hash_2] == -1:
                hash_table2[hash_2] = key
                return True
            key, hash_table2[hash_2] = hash_table2[hash_2], key 

        # If we reach here, then a cycle is detected and we return False
        return False
    
    def rehash(self):
        new_size = self.size * 2 - 1
        new_hash_table1 = [-1] * new_size
        new_hash_table2 = [-1] * new_size
        self.size = new_size
        for key in self.hash_table1 + self.hash_table2:
            if key != -1:
                self.insert(key, new_hash_table1, new_hash_table2)
        return 

    def search(self, key):
        index1 = self.hash1(key)
        if self.hash_table1[index1] == key:
            return True

        index2 = self.hash2(key)
        if self.hash_table2[index2] == key:
            return True

        return False
    
    def test_cuckoo_hashing(self, dataset):
        for key in dataset:
            self.insert(key, self.hash_table1, self.hash_table2)
        print("Cuckoo Hashing Unsuccessful Insert Count: ", self.unsuccessful_insertion_count, "\n")
        return self.unsuccessful_insertion_count

    def print_hash_table(self):
        print(self.hash_table1)
        print(self.hash_table2)

dataset = util.read_dataset()
instance = CuckooHashing()
instance.test_cuckoo_hashing(dataset)

print(instance.search(6041))
