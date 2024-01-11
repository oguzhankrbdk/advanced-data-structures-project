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

    def insert(self, key):
        for _ in range(self.size):
            index1 = self.hash1(key)
            key, self.hash_table1[index1] = self.hash_table1[index1], key
            if key is -1:
                return True

            index2 = self.hash2(key)
            key, self.hash_table2[index2] = self.hash_table2[index2], key
            if key is -1:
                return True

        # If we reach here, then a cycle is detected and we return False
        return False

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
            self.insert(key)
        print("Cuckoo Hashing Unsuccessful Insert Count: ", self.unsuccessful_insertion_count, "\n")
        return self.unsuccessful_insertion_count

    def print_hash_table(self):
        print(self.hash_table1)
        print(self.hash_table2)

dataset = util.read_dataset()
instance = CuckooHashing()
instance.test_cuckoo_hashing(dataset)

print(instance.search(6041))
