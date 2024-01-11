import constants

class CuckooHashing:

    def __init__(self, pair_index):
        self.size = constants.DATASET_SIZE
        self.hash_table = [None] * constants.HASH_TABLE_SIZE
        self.POS = [-1, -1]
        self.pair_index = pair_index
        self.unsuccessful_insert_count = 0

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return (key // self.size) % self.size
    
    def hash_function_3(self, key):
        return (key // self.size**2) % self.size
    
    def choose_hash_function_pair(self, key, pair_index):
        keys = [None] * 2

        if pair_index == 0:
            keys[0] = self.hash_function_1(key)
            keys[1] = self.hash_function_2(key)
        
        elif pair_index == 1:
            keys[0] = self.hash_function_2(key)
            keys[1] = self.hash_function_3(key)
        
        else:
            keys[0] = self.hash_function_1(key)
            keys[1] = self.hash_function_3(key)
        
        return keys

    def place(self, key, table_index):
        for n in range(self.size):
            j = self.choose_hash_function_pair(key, self.pair_index)[0] if table_index == 0 else self.choose_hash_function_pair(key, self.pair_index)[1]
            if self.hash_table[j] is None:
                self.hash_table[j] = key
                self.POS[table_index] = j
                return True
            if self.hash_table[j] == key:
                self.POS[table_index] = j
                return True
            key, self.hash_table[j] = self.hash_table[j], key
            table_index = 1 - table_index
        return False

    def rehash(self, old_table):
        self.size = len(old_table)
        self.hash_table = [None] * self.size
        for i in range(self.size):
            if old_table[i] is not None:
                key = old_table[i]
                if not self.place(key, 0):
                    self.hash_table = old_table
                    return False
        return True

    def insert(self, key):
        if not self.place(key, 0):
            old_table = self.hash_table[:]
            if not self.rehash(old_table):
                return False
        return True

    def search(self, key):
        for i in range(2):
            j = self.choose_hash_function_pair(key, self.pair_index)[0] if i == 0 else self.choose_hash_function_pair(key, self.pair_index)[1]
            if self.hash_table[j] == key:
                return True
        return False

    def delete(self, key):
        for i in range(2):
            j = self.choose_hash_function_pair(key, self.pair_index)[0] if i == 0 else self.choose_hash_function_pair(key, self.pair_index)[1]
            if self.hash_table[j] == key:
                self.hash_table[j] = None
                return True
        return False
    
    def print_hash_table(self):
        print(self.hash_table)
    
    def test_cuckoo_hashing(self, dataset):
        for key in dataset:
            self.insert(key)
        
        print("Cuckoo Hashing for pair index = ", self.pair_index, " Unsuccessful Insert Count: ", self.unsuccessful_insert_count, "\n")
        return self.hash_table