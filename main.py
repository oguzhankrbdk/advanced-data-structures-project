import constants
import linear_probing, quadratic_probing, double_hashing
import util

dataset = util.read_dataset()

linear_probing_instance = linear_probing.LinearProbing()
quadratic_probing_instance = quadratic_probing.QuadraticProbingHash()
double_hashing_instance = double_hashing.DoubleHashing()

linear_probing_instance.test_linear_probing(dataset)
quadratic_probing_instance.test_quadratic_probing(dataset)
double_hashing_instance.test_double_hashing(dataset)