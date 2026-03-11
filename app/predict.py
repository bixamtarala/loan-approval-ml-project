from app.load import load_model
from app.utils import prepare_input

def predict_loan(data):

    model = load_model()

    df = prepare_input(data)

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return prediction, probability