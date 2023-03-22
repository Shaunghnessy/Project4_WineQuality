import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def predict(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):

        x = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])

        filename = 'finalized_model.sav'
        self.model = pickle.load(open(filename, 'rb'))

        proba = self.model.predict_proba(x)[0]

        if proba[0] > proba[1]:
            prediction = "Bad"
        else:
            prediction = "Good"

        return prediction