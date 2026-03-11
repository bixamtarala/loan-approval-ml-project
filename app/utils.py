
import pandas as pd

def prepare_input(data):

    df = pd.DataFrame([data])

    # Feature Engineering (same as training)
    df["Total_Income"] = df["Applicant_Income"] + df["Coapplicant_Income"]

    df["EMI"] = df["Loan_Amount"] / df["Loan_Amount_Term"]

    return df