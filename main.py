import constants
import linear_probing, quadratic_probing, double_hashing
import util

dataset = util.read_dataset()
#dataset = util.generate_random_dataset()

def test_linear_probing(dataset):
    linear_probing_instance = linear_probing.LinearProbing()
    linear_probing_instance.test_linear_probing(dataset)

def test_double_hashing(dataset, draw_graphs):
    execution_times = []
    unsuccessful_insertion_attempts = []
    r_values = [1000000, 617273, 518389, 286753, 68437, 3607]

    for r_value in r_values:
        double_hashing_instance = double_hashing.DoubleHashing(r_value)
        double_hashing_instance.test_double_hashing(dataset)
        execution_times.append(double_hashing_instance.execution_time)
        unsuccessful_insertion_attempts.append(double_hashing_instance.unsuccessful_insertion_attempts)
    if draw_graphs == True:
        util.draw_double_hashing_execution_time_graph(execution_times, r_values)
        util.draw_double_hashing_unsuccessful_insertion_attempts_graph(unsuccessful_insertion_attempts, r_values)

def test_quadratic_probing(dataset, draw_graphs):
    execution_times = []
    unsuccessful_insertion_attempts = []
    parameter_sets = [[1, 1], [1, 13], [2, 68437], [2, 518389], [68437, 518389], [617273, 1000000]]

    for i in range(0, len(parameter_sets)):
        quadratic_probing_instance = quadratic_probing.QuadraticProbingHash(parameter_sets[i])
        quadratic_probing_instance.test_quadratic_probing(dataset)
        execution_times.append(quadratic_probing_instance.execution_time * 1000)
        unsuccessful_insertion_attempts.append(quadratic_probing_instance.unsuccessful_insertion_attempts)
    
    if draw_graphs == True:
        util.draw_quadratic_probing_execution_time_graph(execution_times, parameter_sets)
        util.draw_quadratic_probing_unsuccessful_insertion_attempts_graph(unsuccessful_insertion_attempts, parameter_sets)

def test_unsuccessful_insertion_attempt_comparison(dataset, hash_table_size):
    if hash_table_size != None:
        constants.set_hash_table_size(hash_table_size)
    else:
        constants.set_hash_table_size(990000)
    execution_times = []
    unsuccessful_insertion_attempts = []
    best_parameters = [68437, 518389]
    best_r_value = 617273

    linear_probing_instance = linear_probing.LinearProbing()
    linear_probing_instance.test_linear_probing(dataset)
    execution_times.append(linear_probing_instance.execution_time)
    unsuccessful_insertion_attempts.append(linear_probing_instance.unsuccessful_insertion_attempts)

    double_hashing_instance = double_hashing.DoubleHashing(best_r_value)
    double_hashing_instance.test_double_hashing(dataset)
    execution_times.append(double_hashing_instance.execution_time)
    unsuccessful_insertion_attempts.append(double_hashing_instance.unsuccessful_insertion_attempts)

    quadratic_probing_instance = quadratic_probing.QuadraticProbingHash(best_parameters)
    quadratic_probing_instance.test_quadratic_probing(dataset)
    execution_times.append(quadratic_probing_instance.execution_time)
    unsuccessful_insertion_attempts.append(quadratic_probing_instance.unsuccessful_insertion_attempts)

    
    util.draw_unsuccessful_insertion_attempts_graph(unsuccessful_insertion_attempts)

def test_execution_time_comparison(dataset, hash_table_size):
    if hash_table_size != None:
        constants.set_hash_table_size(hash_table_size)
    else:
        constants.set_hash_table_size(1000000)

    execution_times = []
    best_parameters = [68437, 518389]
    best_r_value = 617273

    linear_probing_instance = linear_probing.LinearProbing()
    linear_probing_instance.test_linear_probing(dataset)
    execution_times.append(linear_probing_instance.execution_time)

    double_hashing_instance = double_hashing.DoubleHashing(best_r_value)
    double_hashing_instance.test_double_hashing(dataset)
    execution_times.append(double_hashing_instance.execution_time)

    quadratic_probing_instance = quadratic_probing.QuadraticProbingHash(best_parameters)
    quadratic_probing_instance.test_quadratic_probing(dataset)
    execution_times.append(quadratic_probing_instance.execution_time)

    util.draw_execution_time_graph(execution_times)

def test_all(dataset, draw_graphs):
    print("HASH TABLE SIZE: ", constants.HASH_TABLE_SIZE, "\n")
    print("DATASET SIZE: ", constants.DATASET_SIZE, "\n")
    test_linear_probing(dataset)
    test_double_hashing(dataset, draw_graphs)
    test_quadratic_probing(dataset, draw_graphs)

def comparisons(dataset, hash_table_size):
    test_unsuccessful_insertion_attempt_comparison(dataset, hash_table_size)
    test_execution_time_comparison(dataset, hash_table_size)

#Set draw_graphs to True to draw graphs
test_all(dataset, False)

#Set hash_table_size to None to use default hash table size
#comparisons(dataset, None)