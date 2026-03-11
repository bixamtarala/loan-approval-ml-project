# Load model
from app.predict import predict_loan

sample_data = {

"Gender":"Male",
"Married":"Yes",
"Dependents":"0",
"Education":"Graduate",
"Self_Employed":"No",
"Applicant_Income":5000,
"Coapplicant_Income":2000,
"Loan_Amount":150,
"Loan_Amount_Term":360,
"Credit_History":1,
"Property_Area":"Urban",
"Total_Income":7000,
"EMI":0.41

}

result = predict_loan(sample_data)

print(result)