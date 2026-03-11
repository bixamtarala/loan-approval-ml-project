import os
import joblib


def load_model():

    model = joblib.load("model/loan_model.pkl")

    return model

