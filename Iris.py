import pandas as pd
import pickle

class Iris:
  def __init__(self):
    self.model_name = "Iris"
    
  def predict(self, X, features_names):
    #logging.info(f"Got request {X} with features {features_names}")        
    df = pd.DataFrame(data=X, columns=features_names)
    # load the model from disk
    #loaded_model = pickle.load(open(filename, 'rb'))
    #result = loaded_model.score(X_test, Y_test)
    #print(result)
    model = pickle.load(open("finalized_model.sav", 'rb'))
    pred = model.predict(df)
    return pred
