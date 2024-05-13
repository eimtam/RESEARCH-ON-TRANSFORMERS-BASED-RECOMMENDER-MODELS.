from experiment_utils import runSingleParameterExperiment, run_recbole
import itertools

weight_decay_values = [0.0001, 0.001, 0.01]
learning_rate_values = [0.0001, 0.001, 0.01]
train_batch_size_values = [256, 1024, 4096]

all_combinations = list(itertools.product(weight_decay_values, learning_rate_values, train_batch_size_values))

for run_iteration, (weight_decay, learning_rate, train_batch_size) in enumerate(all_combinations, start=1):
    if run_iteration > 13:
        parameter_dict = {
            "weight_decay": weight_decay,
            "learning_rate": learning_rate,
            "train_batch_size": train_batch_size
        }
        runSingleParameterExperiment(run_iteration, parameter_dict) 