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

    def metrics(self):
        return [
            {"type": "COUNTER", "key": "mycounter", "value": 1}, # a counter which will increase by the given value
            {"type": "GAUGE", "key": "mygauge", "value": 100},   # a gauge which will be set to given value
            {"type": "TIMER", "key": "mytimer", "value": 20.2},  # a timer which will add sum and count metrics - assumed millisecs
        ]