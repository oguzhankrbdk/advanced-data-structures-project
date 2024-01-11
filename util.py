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

def generate_prime_number(range, type):
    prime_number = 0
    #set min range to half of the range
    if type == "quadratic":
        range_min = range / 2
    else:
        range_min = range / 2
    while True:
        prime_number = random.randint(500000, range)
        if is_prime(prime_number):
            break
    return prime_number


def read_dataset():
    dataset = []
    file = open("unique_numbers.txt", "r")
    for line in file:
        for number in line.split():
            dataset.append(int(number))
    return dataset