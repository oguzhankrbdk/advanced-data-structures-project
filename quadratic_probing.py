import util
import constants

class QuadraticProbingHash:
    constant_1 = 0
    constant_2 = 0
    number_of_collisions = 0
    successful_insertion_count = 0
    unsuccessful_insert_count = 0
    
    def __init__(self):
        self.size = constants.HASH_TABLE_SIZE
        self.hash_table = [-1] * constants.HASH_TABLE_SIZE
        self.parameter_set = self.generate_constant_set()
        self.unsuccessful_insert_count = 0
        self.constant_1 = self.parameter_set[0]
        self.constant_2 = self.parameter_set[1]
        self.number_of_collisions = 0

    def hash(self, key):
        return key % self.size
           
    def insert(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == -1:
            self.hash_table[hash_value] = key
            self.successful_insertion_count += 1
            return True
        else:
            for i in range(self.size):
                self.unsuccessful_insert_count += 1
                new_hash_value = (hash_value + i**2) % self.size
                if self.hash_table[new_hash_value] == -1:
                    self.hash_table[new_hash_value] = key
                    self.successful_insertion_count += 1
                    return True

    def search(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == key:
            return hash_value
        else:
            i = 1
            while True:
                new_hash_value = (hash_value + i**2) % self.size
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
            i = 1
            while True:
                new_hash_value = (hash_value + i**2) % self.size
                if self.hash_table[new_hash_value] == key:
                    self.hash_table[new_hash_value] = None
                    break
                i += 1
                if i == self.size:
                    break

    def print_hash_table(self):
        print(self.hash_table)

    def test_quadratic_probing(self, dataset):
        for key in dataset:
            self.insert(key)
        return self.unsuccessful_insert_count

    def generate_constant_set(self):
        parameter_set = [None] * 2
        for i in range(2):
            temp_val = util.generate_prime_number(constants.HASH_TABLE_SIZE, "quadratic")
            if temp_val not in parameter_set:
                parameter_set[i] = temp_val
            else:
                while temp_val in parameter_set:
                    temp_val = util.generate_prime_number(constants.HASH_TABLE_SIZE, "quadratic")
        return parameter_set
    
    def test_quadratic_probing(self, dataset):
        for key in dataset:
            self.insert(key)

        print("Quadratic Probing for c1 = ", self.constant_1, " and c2 = ", self.constant_2, " the number of unsuccessful insertion count is: ", self.unsuccessful_insert_count, " and the number of successful_insertion_count is : ", self.successful_insertion_count,"\n")
    
    def set_c1(self, c1):
        self.constant_1 = c1
    
    def set_c2(self, c2):
        self.constant_2 = c2
    
    def get_c1(self):
        return self.constant_1
    
    def get_c2(self):
        return self.constant_2
""" 
instance = QuadraticProbingHash()
dataset = util.read_dataset()

instance.test_quadratic_probing(dataset) """