from model import SegModel
from mesa.batchrunner import FixedBatchRunner
import pandas as pd

# parameters that will remain constant
fixed_parameters = {
    "height": 20,
    "width": 20,
    "num_agents": 350,
    "minority_pc": 0.4,
}

# parameters you want to vary
# can also include combinations here
parameters_list = [{"intolerance": 0.25, "wealth_intolerance": 0.25},
                   {"intolerance": 0.25, "wealth_intolerance": 0.5},
                   {"intolerance": 0.25, "wealth_intolerance": 0.75},
                   {"intolerance": 0.5, "wealth_intolerance": 0.25},
                   {"intolerance": 0.5, "wealth_intolerance": 0.5},
                   {"intolerance": 0.5, "wealth_intolerance": 0.75},
                   {"intolerance": 0.75, "wealth_intolerance": 0.25},
                   {"intolerance": 0.75, "wealth_intolerance": 0.5},
                   {"intolerance": 0.75, "wealth_intolerance": 0.75}]

# what to run and what to collect
# iterations is how many runs per parameter value
# max_steps is how long to run the model
batch_run = FixedBatchRunner(SegModel, parameters_list,
                             fixed_parameters, iterations=30,
                             model_reporters={"Pct Happy": lambda m: round(100 * m.happy / m.num_agents, 1),
                                              "Pct Happy Group A": lambda m: round(100 * m.happy0 / m.num_agents0, 1),
                                              "Pct Happy Group B": lambda m: round(100 * m.happy1 / m.num_agents1, 1),
                                              "Avg pct similar neighbors": lambda m: m.pct_neighbors,
                                              "Avg pct similar neighbors (A)": lambda m: m.pct_neighbors0,
                                              "Avg pct similar neighbors (B)": lambda m: m.pct_neighbors1,
                                              "Avg pct similar neighbors (count empty)": lambda m: m.pct_neighbors_e,
                                              "Avg pct similar neighbors (A) (count empty)": lambda
                                                  m: m.pct_neighbors_e0,
                                              "Avg pct similar neighbors (B) (count empty)": lambda
                                                  m: m.pct_neighbors_e1,
                                              "Num Agents": lambda m: m.num_agents,
                                              "Num Agents (A)": lambda m: m.num_agents0,
                                              "Num Agents (B)": lambda m: m.num_agents1},
                            agent_reporters={"Type": "type"},
                             max_steps=50)

# run the batches of your model with the specified variations
batch_run.run_all()


## NOTE: to do data collection, you need to be sure your pathway is correct to save this!
# Data collection
# extract data as a pandas Data Frame
ordered_dict = batch_run.get_collector_model()
step_dict = {'Intolerance':[], 'wealth_intolerance':[], 'Avg pct similar neighbors':[]}
for key, value in ordered_dict.items():
    for i in value['Avg pct similar neighbors']:
        step_dict['Intolerance'].append(key[0])
        step_dict['wealth_intolerance'].append(key[1])
        step_dict['Avg pct similar neighbors'].append(i)

step_df = pd.DataFrame(step_dict)
step_df.to_csv('data/batch_run.csv')