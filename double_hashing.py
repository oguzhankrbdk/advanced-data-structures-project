import constants
import util

class DoubleHashing:
    def __init__(self):
        self.size = constants.HASH_TABLE_SIZE
        self.hash_table = [-1] * constants.HASH_TABLE_SIZE
        self.unsuccessful_insertion_count = 0
        self.r_value = self.generate_r_value()
        self.successful_insertion_count = 0
    
    def hash_function_1(self, key):
        hash1 = key % self.size
        return hash1
    
    def hash_function_2(self, key):
        hash2 = self.r_value - (key % self.r_value)
        return hash2
    
    def insert(self, key):
        index = self.hash_function_1(key)
        if self.hash_table[index] == -1:
            self.hash_table[index] = key
            self.successful_insertion_count += 1
            return True
        else:
            i = 1
            while True:
                self.unsuccessful_insertion_count += 1
                new_hash_value = (index + i * self.hash_function_2(key)) % self.size
                if self.hash_table[new_hash_value] == -1:
                    self.hash_table[new_hash_value] = key
                    self.successful_insertion_count += 1
                    return True
                i += 1
                if i == self.size:
                    return False
    
    def search(self, key):
        hash_value = self.hash_function_1(key)
        if self.hash_table[hash_value] == key:
            return hash_value
        else:
            i = 1
            while True:
                new_hash_value = (hash_value + i * self.hash_function_2(key)) % self.size
                if self.hash_table[new_hash_value] == key:
                    return new_hash_value
                i += 1
                if i == self.size:
                    return None
    
    def print_hash_table(self):
        print(self.hash_table)
    
    def generate_r_value(self):
        return util.generate_prime_number(self.size, "double")
    
    def test_double_hashing(self, dataset):
        for key in dataset:
            self.insert(key)
        print("Double Hashing for r = ", self.r_value, " Unsuccessful Insertion Count: ", self.unsuccessful_insertion_count, " Succesful Insertion Count: ", self.successful_insertion_count,"\n")
        return self.unsuccessful_insertion_count
""" 
instance = DoubleHashing()
dataset = util.read_dataset()
# print(dataset)

instance.test_double_hashing(dataset) """