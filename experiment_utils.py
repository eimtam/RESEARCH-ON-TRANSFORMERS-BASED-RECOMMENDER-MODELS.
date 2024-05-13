from recbole.quick_start import run_recbole
import wandb

def extract_project_name(config_file_name):
    project_suffix = ""
    base_name = config_file_name.replace("config", "").replace(".yaml", "") 
    return project_suffix + base_name

def run_experiment(name, model_name, dataset_name, config_file_name, sent_config):
    projectName=extract_project_name(config_file_name)
    wandb.init(project=projectName, name=name)
    run_recbole(model=model_name, dataset=dataset_name, config_file_list=[config_file_name], config_dict=sent_config)
    wandb.finish()

def runSingleParameterExperiment(run_iteration, parameter_dict):
    run_id = f"ID{run_iteration}"
    run_experiment_on_model("BERT4Rec", run_id, parameter_dict)

def run_experiment_on_model(model_name, run_id, parameter_dict):
    name = combine_and_format_name(model_name, run_id, parameter_dict)
    run_experiment(name=name, model_name=model_name, dataset_name="movies", config_file_name="configMovies.yaml" , sent_config=parameter_dict)
    
    name = combine_and_format_name(model_name, run_id, parameter_dict)
    run_experiment(name=name, model_name=model_name, dataset_name="rent", config_file_name="configRent.yaml"  , sent_config=parameter_dict) 
    
def combine_and_format_name(model_name, run_id, parameter_dict):
    param_string = " | ".join([str(v) for v in parameter_dict.values()])
    return f"{model_name}-{run_id} ({param_string})"