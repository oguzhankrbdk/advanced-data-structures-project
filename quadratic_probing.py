import util
import constants

class QuadraticProbingHash:
    unseccessful_insert_count = 0

    def __init__(self, size):
        self.size = constants.DATASET_SIZE
        self.hash_table = [None] * constants.HASH_TABLE_SIZE
        self.parameter_set = self.generate_constant_set()

    def hash(self, key):
        c1 = self.parameter_set[0]
        c2 = self.parameter_set[1]
        i = 0
        while True:
            hash_value = (key + c1 * i + c2 * i**2) % self.size
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
        return self.unseccessful_insert_count

    def generate_constant_set(self):
        parameter_set = [None] * 2
        for i in range(2):
            temp_val = util.generate_prime_number(constants.HASH_TABLE_SIZE)
            if temp_val not in parameter_set:
                parameter_set.append(temp_val)
            else:
                while temp_val in parameter_set:
                    temp_val = util.generate_prime_number(constants.HASH_TABLE_SIZE)
        return parameter_set
    
    def test_quadratic_probing(self, dataset):
        for key in dataset:
            self.insert(key)
        print("For c1 = ", self.parameter_set[0], " and c2 = ", self.parameter_set[1], " the number of unseccessful insertions is: ", self.unseccessful_insert_count, ".")
        return self.unseccessful_insert_count