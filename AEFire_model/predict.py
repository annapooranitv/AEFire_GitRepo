import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Union
import pandas as pd
import numpy as np

from AEFire_model import __version__ as _version
from AEFire_model.config.core import config
from AEFire_model.pipeline import AEFire_pipe
from AEFire_model.processing.data_manager import load_pipeline
#from AEFire_model.processing.data_manager import pre_pipeline_preparation
from AEFire_model.processing.validation import validate_inputs


pipeline_file_name = f"{config.app_config_.pipeline_save_file}{_version}.pkl"
AEFire_pipe= load_pipeline(file_name=pipeline_file_name)


def make_prediction(*,input_data:Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model """

    validated_data, errors = validate_inputs(input_df=pd.DataFrame(input_data))
   
    results = {"predictions": None, "version": _version, "errors": errors}
    
    predictions = AEFire_pipe.predict(validated_data)
    
    results = {"predictions": predictions,"version": _version, "errors": errors}
    
    if not errors:

        predictions = AEFire_pipe.predict(validated_data)
        print(predictions)
        results = {"predictions": predictions,"version": _version, "errors": errors}
        #print(results)
    
    return results

if __name__ == "__main__":

    data_in={'SIZE':[7],'FUEL':["lpg"],'DISTANCE':[10],'DESIBEL':[103],'AIRFLOW':[9.7],'FREQUENCY':[65]}
    
    make_prediction(input_data=data_in)
