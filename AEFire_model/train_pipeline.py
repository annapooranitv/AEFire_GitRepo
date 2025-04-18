import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from AEFire_model.config.core import config
from AEFire_model.pipeline import AEFire_pipe
from AEFire_model.processing.data_manager import load_dataset, save_pipeline

def run_training() -> None:
    
    """
    Train the model.
    """

    # read training data
    data = load_dataset(file_name=config.app_config_.training_data_file)
    print('111: ', type(data[config.model_config_.features]))
    print('222: ', type(data[config.model_config_.target]))
    print('333: ', type(config.model_config_.test_size))
    print('444: ', type(config.model_config_.random_state))
    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config_.features],  # predictors
        data[config.model_config_.target],
        test_size= config.model_config_.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state= config.model_config_.random_state,
    )

    # Pipeline fitting
    AEFire_pipe.fit(X_train,y_train)
    #y_pred = AEFire_pipe.predict(X_test)
    #print("Accuracy(in %):", accuracy_score(y_test, y_pred)*100)

    # persist trained model
    save_pipeline(pipeline_to_persist= AEFire_pipe)
    # printing the score
    
if __name__ == "__main__":
    run_training()
