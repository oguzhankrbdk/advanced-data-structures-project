def double_hashing_hash(key, size):
    hash1 = key % size
    hash2 = 1 + (key % (size - 1))
    i = 0
    while True:
        hash_value = (hash1 + i * hash2) % size
        if hash_value < size:
            return hash_value
        i += 1