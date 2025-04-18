import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier  

from AEFire_model.config.core import config
from AEFire_model.processing.features import fuelImputer
from AEFire_model.processing.features import Mapper
#from titanic_model.processing.features import age_col_tfr

AEFire_pipe=Pipeline([
    ("fuel_imputation", fuelImputer(variables=config.model_config_.fuel_var)
     ),
     ("map_fuel", Mapper(config.model_config_.fuel_var, config.model_config_.fuel_mappings )
     ),
    # scale
     ("scaler", StandardScaler()),
     ('model_rf', DecisionTreeClassifier(min_samples_leaf=config.model_config_.min_samples_leaf, 
                                         max_depth=config.model_config_.max_depth, 
                                         max_features=config.model_config_.max_features,
                                         random_state=config.model_config_.random_state))
          
     ])
