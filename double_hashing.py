import constants
import util

class DoubleHashing:

    def __init__(self):
        self.size = constants.DATASET_SIZE
        self.hash_table = [None] * constants.HASH_TABLE_SIZE
        self.r_value = 17
        self.unseccessful_insert_count = 0
        
    def hash(self, key):
        hash1 = key % self.size
        hash2 = self.r_value - (key % self.r_value)
        i = 0
        while True:
            hash_value = (hash1 + i * hash2) % self.size
            if hash_value < self.size:
                return hash_value
            i += 1

    def insert(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = key
        else:
            self.unseccessful_insert_count += 1
    
    def search(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == key:
            return hash_value
        else:
            i = 0
            while True:
                new_hash_value = (hash_value + i) % self.size
                if self.hash_table[new_hash_value] == key:
                    return new_hash_value
                i += 1
                if i == self.size:
                    return None
    
    def delete(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == key:
            self.hash_table[hash_value] = None
        else:
            i = 0
            while True:
                new_hash_value = (hash_value + i) % self.size
                if self.hash_table[new_hash_value] == key:
                    self.hash_table[new_hash_value] = None
                    break
                i += 1
                if i == self.size:
                    break

    def print_hash_table(self):
        print(self.hash_table)
    
    def generate_r_value(self):
        return util.generate_prime_number(self.size, "double")
    
    def test_double_hashing(self, dataset):
        for key in dataset:
            self.insert(key)
        print("Double Hashing for r = ", self.r_value, " Unseccessful Insert Count: ", self.unseccessful_insert_count, "\n")
        return self.unseccessful_insert_count