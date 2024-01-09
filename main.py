import constants
import linear_probing, quadratic_probing, double_hashing
import util

dataset = util.generate_random_dataset(constants.DATASET_SIZE)

linear_probing_hash = linear_probing.LinearProbingHash()
linear_probing_hash.test_linear_probing(dataset)

dataset = util.generate_random_dataset(constants.DATASET_SIZE)

quadratic_probing_hash = quadratic_probing.QuadraticProbingHash()
quadratic_probing_hash.test_quadratic_probing(dataset)

dataset = util.generate_random_dataset(constants.DATASET_SIZE)

double_hashing_hash = double_hashing.DoubleHashing()
double_hashing_hash.test_double_hashing(dataset)