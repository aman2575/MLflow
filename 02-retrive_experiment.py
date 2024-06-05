import mlflow
from mlflow_utils import get_mlflow_experiment

if __name__ == "__main__":
    experiment = get_mlflow_experiment(experiment_name="Default")

    print("Name: {}".format(experiment.name))
    print("Experiment_id: {}".format(experiment.experiment_id))
    print("Artifact Location: {}".format(experiment.artifact_location))
    print("Tags: {}".format(experiment.tags))
    print("Lifecycle_stag: {}".format(experiment.lifecycle_stage))
    print("Creation timestamp: {}".format(experiment.creation_time))