from app.load import load_model
from app.utils import prepare_input

def predict_loan(data):

    model = load_model()

    df = prepare_input(data)

    prediction = model.predict(df)[0]

    if prediction == 1:
        return "Loan Approved"
    else:
        return "Loan Rejected"