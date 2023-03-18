import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        # Load the model during initialization
        self.model = pickle.load(open('finalized_model.sav', 'rb'))
        
    def predict(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, 
                pH, sulphates, alcohol):
    
        data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                          chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, 
                          pH, sulphates, alcohol]])
    
        pred = self.model.predict(data)[0]
        
        if pred == 0:
            prediction = "Bad"
        else:
            prediction = "Good"
    
        return prediction