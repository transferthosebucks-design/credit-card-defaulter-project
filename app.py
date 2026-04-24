from flask import Flask, render_template, request
import pandas as pd
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

education_mapping = {
    "Graduate School": 1,
    "University": 2,
    "High School": 3,
    "Others": 4
}
marriage_mapping = {
    "Married": 1,
    "Single": 2,
    "Others": 3
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Get data from form
        limit_bal = int(request.form["limit_bal"])
        sex = 1 if request.form["sex"] == "Male" else 2
        education = education_mapping[request.form["education"]]
        marriage = marriage_mapping[request.form["marriage"]]
        age = int(request.form["age"])
        pay_status_sept = int(request.form["pay_status_sept"])
        pay_status_aug = int(request.form["pay_status_aug"])
        pay_status_jul = int(request.form["pay_status_jul"])
        pay_status_jun = int(request.form["pay_status_jun"])
        pay_status_may = int(request.form["pay_status_may"])
        pay_status_apr = int(request.form["pay_status_apr"])
        bill_amt_sept = int(request.form["bill_amt_sept"])
        bill_amt_aug = int(request.form["bill_amt_aug"])
        bill_amt_jul = int(request.form["bill_amt_jul"])
        bill_amt_jun = int(request.form["bill_amt_jun"])
        bill_amt_may = int(request.form["bill_amt_may"])
        bill_amt_apr = int(request.form["bill_amt_apr"])
        pay_amt_sept = int(request.form["pay_amt_sept"])
        pay_amt_aug = int(request.form["pay_amt_aug"])
        pay_amt_jul = int(request.form["pay_amt_jul"])
        pay_amt_jun = int(request.form["pay_amt_jun"])
        pay_amt_may = int(request.form["pay_amt_may"])
        pay_amt_apr = int(request.form["pay_amt_apr"])

        # Create DataFrame for the input data
        user_input_data = pd.DataFrame({
            "LIMIT_BAL": [limit_bal],
            "SEX": [sex],
            "EDUCATION": [education],
            "MARRIAGE": [marriage],
            "AGE": [age],
            "PAY_0": [pay_status_sept],
            "PAY_2": [pay_status_aug],
            "PAY_3": [pay_status_jul],
            "PAY_4": [pay_status_jun],
            "PAY_5": [pay_status_may],
            "PAY_6": [pay_status_apr],
            "BILL_AMT1": [bill_amt_sept],
            "BILL_AMT2": [bill_amt_aug],
            "BILL_AMT3": [bill_amt_jul],
            "BILL_AMT4": [bill_amt_jun],
            "BILL_AMT5": [bill_amt_may],
            "BILL_AMT6": [bill_amt_apr],
            "PAY_AMT1": [pay_amt_sept],
            "PAY_AMT2": [pay_amt_aug],
            "PAY_AMT3": [pay_amt_jul],
            "PAY_AMT4": [pay_amt_jun],
            "PAY_AMT5": [pay_amt_may],
            "PAY_AMT6": [pay_amt_apr]
        })

        # Make prediction
        predicted_default = model.predict(user_input_data)
        
        # Interpret the prediction
        if predicted_default[0] == 1:
            prediction = "The model predicts that the client may default on their credit card payment."
        else:
            prediction = "The model predicts that the client is unlikely to default on their credit card payment."

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
