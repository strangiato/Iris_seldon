import pandas as pd
import pickle


class Iris:
    def __init__(self):
        self.model_name = "Iris"

        # load the model from disk
        self.model = pickle.load(open("finalized_model.sav", "rb"))

    def predict(self, X, features_names):
        df = pd.DataFrame(data=X, columns=features_names)
        
        pred = self.model.predict(df)
        return pred
