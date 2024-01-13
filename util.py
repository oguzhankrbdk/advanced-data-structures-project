import random
import math
import constants
import matplotlib.pyplot as plt
import numpy as np

def generate_random_dataset():
    dataset = []
    for i in range(constants.DATASET_SIZE):
        dataset.append(random.randint(0, 1000000))
    return dataset

dataset = generate_random_dataset()

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
        prime_number = random.randint(3000, 5000)
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

def draw_unsuccessful_insertion_count_graph(input_data):
   
    data = {'Linear Probing':input_data[0], 'Double Hashing':input_data[1], 'Quadratic Probing':input_data[2],}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("Hashing Methods")
    plt.ylabel("Unsuccessful Insertion Counts")
    plt.title("Unsuccessful Insertion Count Comparison")
    plt.show()

def draw_unsuccessful_insertion_attempts_graph(input_data):
    data = {'Linear Probing %d Attempts'%input_data[0]:input_data[0], 'Double Hashing %d Attempts'%input_data[1]:input_data[1], 'Quadratic Probing %d Attempts'%input_data[2]:input_data[2],}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("Hashing Methods")
    plt.ylabel("Unsuccessful Insertion Attempts")
    plt.title("Unsuccessful Insertion Attempt Comparison For Hash Table Size %d Dataset Size %d" %(constants.HASH_TABLE_SIZE, constants.DATASET_SIZE))
    plt.savefig('graphs/unsuccessful_insertion_attempts_graph.png')
    plt.show()

def draw_quadratic_probing_execution_time_graph(input_data, parameter_sets):
    data = {'c1 = %d, c2 = %d' %(parameter_sets[0][0], parameter_sets[0][1]):input_data[0], 'c1 = %d, c2 = %d' %(parameter_sets[1][0], parameter_sets[1][1]):input_data[1],
            'c1 = %d, c2 = %d' %(parameter_sets[2][0], parameter_sets[2][1]):input_data[2], 'c1 = %d, c2 = %d' %(parameter_sets[3][0], parameter_sets[3][1]):input_data[3],
            'c1 = %d, c2 = %d' %(parameter_sets[4][0], parameter_sets[4][1]):input_data[4], 'c1 = %d, c2 = %d' %(parameter_sets[5][0], parameter_sets[5][1]):input_data[5]}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("c1, c2 Values")
    plt.ylabel("Execution Times(Milliseconds)")
    plt.title("Quadratic Probing Execution Time Comparison For Hash Table Size %d Dataset Size %d" %(constants.HASH_TABLE_SIZE, constants.DATASET_SIZE))
    plt.savefig('graphs/quadratic_probing_execution_time_graph.png')
    plt.show()

def draw_quadratic_probing_unsuccessful_insertion_attempts_graph(input_data, parameter_sets):
    data = {'c1 = %d, c2 = %d' %(parameter_sets[0][0], parameter_sets[0][1]):input_data[0], 'c1 = %d, c2 = %d' %(parameter_sets[1][0], parameter_sets[1][1]):input_data[1],
            'c1 = %d, c2 = %d' %(parameter_sets[2][0], parameter_sets[2][1]):input_data[2], 'c1 = %d, c2 = %d' %(parameter_sets[3][0], parameter_sets[3][1]):input_data[3],
            'c1 = %d, c2 = %d' %(parameter_sets[4][0], parameter_sets[4][1]):input_data[4], 'c1 = %d, c2 = %d' %(parameter_sets[5][0], parameter_sets[5][1]):input_data[5]}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("c1, c2 Values")
    plt.ylabel("Unsuccessful Insertion Attempts")
    plt.title("Quadratic Probing Unsuccessful Insertion Attempts Comparison For Hash Table Size %d Dataset Size %d" %(constants.HASH_TABLE_SIZE, constants.DATASET_SIZE))
    plt.savefig('graphs/quadratic_probing_unsuccessful_insertion_attempts_graph.png')
    plt.show()


def draw_double_hashing_execution_time_graph(input_data, r_values):
    data = {'r = %d' % r_values[0]:input_data[0], 'r = %d' % r_values[1]:input_data[1], 'r = %d' % r_values[2]:input_data[2], 
            'r = %d' % r_values[3]:input_data[3], 'r = %d' % r_values[4]:input_data[4], 'r = %d' % r_values[5]:input_data[5]}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("r Values")
    plt.ylabel("Execution Times(Seconds)")
    plt.title("Double Hashing Execution Time Comparison For Hash Table Size %d Dataset Size %d" %(constants.HASH_TABLE_SIZE, constants.DATASET_SIZE))
    plt.savefig('graphs/double_hashing_execution_time_graph.png')
    plt.show()

def draw_double_hashing_unsuccessful_insertion_attempts_graph(input_data, r_values):
    data = {'r = %d' % r_values[0]:input_data[0], 'r = %d' % r_values[1]:input_data[1], 'r = %d' % r_values[2]:input_data[2], 
            'r = %d' % r_values[3]:input_data[3], 'r = %d' % r_values[4]:input_data[4], 'r = %d' % r_values[5]:input_data[5]}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("r Values")
    plt.ylabel("Unsuccessful Insertion Attempts")
    plt.title("Double Hashing Unsuccessful Insertion Attempts Comparison For Hash Table Size %d Dataset Size %d" %(constants.HASH_TABLE_SIZE, constants.DATASET_SIZE))
    plt.savefig('graphs/double_hashing_unsuccessful_insertion_attempts_graph.png')
    plt.show()

def draw_execution_time_graph(input_data):
    data = {'Linear Probing':input_data[0], 'Double Hashing':input_data[1], 'Quadratic Probing':input_data[2],}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("Hashing Methods")
    plt.ylabel("Execution Times(Milliseconds)")
    plt.title("Execution Time Comparison For Hash Table Size %d Dataset Size %d" %(constants.HASH_TABLE_SIZE, constants.DATASET_SIZE))
    plt.savefig('graphs/execution_time_graph.png')
    plt.show()