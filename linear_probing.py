import util
import constants

class LinearProbing:
    def __init__(self):
        self.size = constants.HASH_TABLE_SIZE
        self.hash_table = [-1] * constants.HASH_TABLE_SIZE
        self.unsuccessful_insertion_count = 0
        self.successful_insertion_count = 0
    
    def hash(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash(key)

        if self.hash_table[index] == -1:
            self.hash_table[index] = key
            self.successful_insertion_count += 1
            return True
        else:
            while True:
               
                new_index = (index + 1) % self.size
                if self.hash_table[new_index] == -1:
                    self.hash_table[new_index] = key
                    self.successful_insertion_count += 1
                    return True
                if new_index == self.size:
                    #print("Hash table is full")
                    self.unsuccessful_insertion_count += 1
                    return False
                else:
                    #print("zort", new_index)
                    self.unsuccessful_insertion_count += 1
                    return False
    def search(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == key:
            return hash_value
        else:
            i = 1
            while True:
                new_hash_value = (hash_value + i) % self.size
                if self.hash_table[new_hash_value] == key:
                    return new_hash_value
                i += 1
                if i == self.size:
                    return None
    
    def test_linear_probing(self, dataset):
        for key in dataset:
            self.insert(key)
        print("Linear Probing Unsuccessful Insertion Count: ", self.unsuccessful_insertion_count, " Successful insertion Count: ", self.successful_insertion_count,"\n")
        return self.unsuccessful_insertion_count
    
    def print_hash_table(self):
        print(self.hash_table)
    
""" instance = LinearProbing()
dataset = util.read_dataset()
#print(dataset)


#print(instance.unsuccessful_insertion_count)
#instance.print_hash_table()
#print(instance.hash_table[18])
instance.test_linear_probing(dataset)
 """
""" for key in instance.hash_table:
    if key != -1:
        print(key) """