import constants

class LinearProbingHash:

    def __init__(self):
        self.size = constants.DATASET_SIZE
        self.hash_table = [None] * constants.HASH_TABLE_SIZE
        self.unseccessful_insert_count = 0

    def hash(self, key):
        return key % self.size

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
            i = 1
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

    def test_linear_probing(self, dataset):
        for key in dataset:
            self.insert(key)
        print("Linear Probing Unseccessful Insert Count: ", self.unseccessful_insert_count, "\n")
        return self.unseccessful_insert_count