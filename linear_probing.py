import time
import constants

class LinearProbing:
    def __init__(self):
        self.size = constants.HASH_TABLE_SIZE
        self.hash_table = [-1] * constants.HASH_TABLE_SIZE
        self.unsuccessful_insertion_count = 0
        self.successful_insertion_count = 0
        self.unsuccessful_insertion_attempts = 0
        execution_time = 0
    
    def hash(self, key):
        return key % self.size
    
    def insert(self, key):
        hash_value = self.hash(key)

        if self.hash_table[hash_value] == -1:
            self.hash_table[hash_value] = key
            self.successful_insertion_count += 1
            return True
        else:
            collision_count = 1
            while True:
                self.unsuccessful_insertion_attempts += 1
                new_hash_value = (hash_value + collision_count) % self.size
                if self.hash_table[new_hash_value] == -1:
                    self.hash_table[new_hash_value] = key
                    self.successful_insertion_count += 1
                    return True
                collision_count += 1
                if new_hash_value >= self.size:
                    self.unsuccessful_insertion_count += 1
                    return False
                
    def search(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == key:
            return hash_value
        else:
            collision_count = 1
            while True:
                new_hash_value = (hash_value + collision_count) % self.size
                if self.hash_table[new_hash_value] == key:
                    return new_hash_value
                collision_count += 1
                if collision_count >= self.size:
                    return None
    
    def delete(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == key:
            self.hash_table[hash_value] = None
        else:
            collision_count = 1
            while True:
                new_hash_value = (hash_value + collision_count) % self.size
                if self.hash_table[new_hash_value] == key:
                    self.hash_table[new_hash_value] = None
                    break
                collision_count += 1
                if collision_count >= self.size:
                    break

    def test_linear_probing(self, dataset):
        start = time.time()
        for key in dataset:
            self.insert(key)
        end = time.time()
        self.execution_time = end - start
        print("Linear Probing Unsuccessful Insertion Count: ", self.unsuccessful_insertion_count, "Unsuccesful Insertion Attempt Count: "
              , self.unsuccessful_insertion_attempts," Successful insertion Count: ", self.successful_insertion_count, " Execution Time: ", self.execution_time, "\n")
        return self.execution_time
    
    def print_hash_table(self):
        print(self.hash_table)
