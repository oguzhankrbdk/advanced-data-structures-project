import constants
import linear_probing, quadratic_probing, double_hashing
import util
import matplotlib.pyplot as plt

dataset = util.read_dataset()
#dataset = util.generate_random_dataset()

def test_linear_probing(dataset):
    linear_probing_instance = linear_probing.LinearProbing()
    linear_probing_instance.test_linear_probing(dataset)

def test_double_hashing(dataset):
    r_values = [1000000, 617273, 518389, 286753, 68437, 2]

    for r_value in r_values:
        double_hashing_instance = double_hashing.DoubleHashing(r_value)
        double_hashing_instance.test_double_hashing(dataset)

def test_quadratic_probing(dataset):
    parameter_sets = [[1, 1], [1, 13], [2, 68437], [2, 518389], [68437, 518389], [617273, 1000000]]

    for i in range(0, len(parameter_sets)):
        quadratic_probing_instance = quadratic_probing.QuadraticProbingHash(parameter_sets[i])
        quadratic_probing_instance.test_quadratic_probing(dataset)


def test_all(dataset):
    print("HASH TABLE SIZE: ", constants.HASH_TABLE_SIZE, "\n")
    print("DATASET SIZE: ", constants.DATASET_SIZE, "\n")
    test_linear_probing(dataset)
    test_double_hashing(dataset)
    test_quadratic_probing(dataset)

test_all(dataset)