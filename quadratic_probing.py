import util
import constants

class QuadraticProbingHash:
    constant_1 = 0
    constant_2 = 0
    successful_insertion_count = 0
    unsuccessful_insertion_count = 0
    
    def __init__(self, parameter_set):
        self.size = constants.HASH_TABLE_SIZE
        self.hash_table = [-1] * constants.HASH_TABLE_SIZE
        self.parameter_set = parameter_set
        self.unsuccessful_insertion_count = 0
        self.constant_1 = self.parameter_set[0]
        self.constant_2 = self.parameter_set[1]
        self.unsuccessful_insertion_attempts = 0

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
                new_hash_value = (hash_value + self.constant_1 * collision_count + self.constant_2 * collision_count**2) % self.size
                if self.hash_table[new_hash_value] == -1:
                    self.hash_table[new_hash_value] = key
                    self.successful_insertion_count += 1
                    return True
                collision_count += 1
                if collision_count >= self.size:
                    self.unsuccessful_insertion_count += 1
                    return False

    def search(self, key):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] == key:
            return hash_value
        else:
            collision_count = 1
            while True:
                new_hash_value = (hash_value + self.constant_1 * collision_count + self.constant_2 * collision_count**2) % self.size
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
                new_hash_value = (hash_value + self.constant_1 * collision_count + self.constant_2 * collision_count**2) % self.size
                if self.hash_table[new_hash_value] == key:
                    self.hash_table[new_hash_value] = None
                    break
                collision_count += 1
                if collision_count >= self.size:
                    break

    def print_hash_table(self):
        print(self.hash_table)

    def test_quadratic_probing(self, dataset):
        for key in dataset:
            self.insert(key)
        return self.unsuccessful_insertion_count

    def generate_constant_set(self):
        parameter_set = [None] * 2
        for i in range(2):
            temp_val = util.generate_prime_number()
            if temp_val not in parameter_set:
                parameter_set[i] = temp_val
            else:
                while temp_val in parameter_set:
                    temp_val = util.generate_prime_number()
        return parameter_set
    
    def test_quadratic_probing(self, dataset):
        for key in dataset:
            self.insert(key)

        print("Quadratic Probing for c1 = ", self.constant_1, " and c2 = ", self.constant_2, " Unsuccessful Insertion Count: ", self.unsuccessful_insertion_count, "Unsuccesful Insertion Attempt Count: ", self.unsuccessful_insertion_attempts," Succesful Insertion Count: ", self.successful_insertion_count,"\n")
        return self.unsuccessful_insertion_count
    
    def set_c1(self, c1):
        self.constant_1 = c1
    
    def set_c2(self, c2):
        self.constant_2 = c2
    
    def get_c1(self):
        return self.constant_1
    
    def get_c2(self):
        return self.constant_2