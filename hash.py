def linear_probing_hash(key, size):
    return key % size

def quadratic_probing_hash(key, size):
    c1 = 1
    c2 = 1
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

# Example usage
key = 42
size = 10

linear_probing_hash_code = linear_probing_hash(key, size)
quadratic_probing_hash_code = quadratic_probing_hash(key, size)
double_hashing_hash_code = double_hashing_hash(key, size)
cuckoo_hashing_hash_code = cuckoo_hashing_hash(key, size)

print("Linear Probing Hash Code:", linear_probing_hash_code)
print("Quadratic Probing Hash Code:", quadratic_probing_hash_code)
print("Double Hashing Hash Code:", double_hashing_hash_code)
print("Cuckoo Hashing Hash Code:", cuckoo_hashing_hash_code)
