import random
import math
import constants
def generate_random_dataset(size):
    dataset = []
    for i in range(size):
        dataset.append(random.randint(0, 1000000))
    return dataset

dataset = generate_random_dataset(constants.DATASET_SIZE)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_number(range):
    prime_number = 0
    #set min range to half of the range
    range_min = range / 2
    while True:
        prime_number = random.randint(range_min, range)
        if is_prime(prime_number):
            break
    return prime_number


