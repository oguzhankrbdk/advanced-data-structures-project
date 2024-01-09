import matplotlib.pyplot as plt
import random
import math

DATASET_SIZE = 600000
HASH_TABLE_SIZE = 1000000

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_number():
    prime_number = 0
    while True:
        prime_number = random.randint(0, 10000)
        if is_prime(prime_number):
            break
    return prime_number

def generate_random_dataset(size):
    dataset = []
    for i in range(size):
        dataset.append(random.randint(0, 1000000))
    return dataset

def linear_probing_hash(key, size):
    return key % size

def quadratic_probing_hash(key, size):
    c1 = generate_prime_number()
    c2 = generate_prime_number()
    i = 0
    while True:
        hash_value = (key + c1 * i + c2 * i**2) % size
        if hash_value < size:
            return hash_value
        i += 1

def double_hashing_hash(key, size):
    hash1 = key % size
    hash2 = 1 + (key % (size - 1))
    i = 0
    while True:
        hash_value = (hash1 + i * hash2) % size
        if hash_value < size:
            return hash_value
        i += 1

def cuckoo_hashing_hash(key, size):
    hash1 = key % size
    hash2 = 1 + (key % (size - 1))
    hash_value = hash1
    for i in range(size):
        if i % 2 == 0:
            hash_value = (hash_value + hash1) % size
        else:
            hash_value = (hash_value + hash2) % size
        if hash_value < size:
            return hash_value


dataset = generate_random_dataset(DATASET_SIZE)

def test_quadratic_probing():
    hash_table = [None] * HASH_TABLE_SIZE
    count = 0
    for key in dataset:
        hash_value = quadratic_probing_hash(key, DATASET_SIZE)
        if hash_table[hash_value] is None:
            hash_table[hash_value] = key
        else:
            #print("Collision detected for key:", key)
            count += 1
    #print_hash_table(hash_table)
    print(count)

def print_hash_table(hash_table):
    for i in range(len(hash_table)):
        print(i, hash_table[i])


# Example usage
key = 42
size = 10

""" linear_probing_hash_code = linear_probing_hash(key, size)
quadratic_probing_hash_code = quadratic_probing_hash(key, size)
double_hashing_hash_code = double_hashing_hash(key, size)
cuckoo_hashing_hash_code = cuckoo_hashing_hash(key, size)

print("Linear Probing Hash Code:", linear_probing_hash_code)
print("Quadratic Probing Hash Code:", quadratic_probing_hash_code)
print("Double Hashing Hash Code:", double_hashing_hash_code)
print("Cuckoo Hashing Hash Code:", cuckoo_hashing_hash_code) """
test_quadratic_probing()

def count_dataset_range(dataset, start, end):
    count = 0
    for i in range(len(dataset)):
        if dataset[i] >= start and dataset[i] <= end:
            count += 1
    return count

def generate_range_array(dataset, range_size):
    range_array = []
    for i in range(0, DATASET_SIZE, range_size):
        range_array.append(count_dataset_range(dataset, i, i + range_size))
    return range_array

range_array = generate_range_array(dataset, 1000000)
second_array = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
for x in range_array:
    print(x)

plt.scatter(range_array, second_array)
plt.show() 