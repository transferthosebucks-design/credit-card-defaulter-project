# Credit Card Default Prediction

A machine learning web application that predicts whether a credit card client is likely to default on the next payment, based on demographic details, repayment history, bill amounts, and previous payment amounts.

## Project Overview

This project combines:
- A trained machine learning model (`model.pkl`)
- A Flask backend (`app.py`)
- An HTML form UI (`templates/index.html`)
- The UCI credit card dataset (`UCI_Credit_Card.csv`)

Users enter customer profile and repayment-related values in the web form, and the application returns a prediction message about default risk.

## Features

- Predicts credit card default risk from 23 input features
- Simple web form interface for fast testing
- Real-time model inference using Flask
- Notebook included for data analysis/model workflow

## Tech Stack

- Python
- Flask
- pandas
- scikit-learn (model loading/inference)
- HTML (Jinja templates)

## Repository Structure

```text
Credit Card Default Prediction/
|- app.py
|- model.pkl
|- UCI_Credit_Card.csv
|- Credit Card Default Prediction Using Python.ipynb
|- templates/
|  |- index.html
|- README.md
|- .gitignore
```

## How It Works

1. The user submits the form from the home page.
2. `app.py` maps categorical values (education, marriage, sex) to model-compatible numeric values.
3. Input values are arranged into a pandas DataFrame.
4. The pre-trained model (`model.pkl`) predicts default (`1`) or non-default (`0`).
5. The prediction result is shown back on the web page.

## Run Locally

### 1) Clone the repository

```bash
git clone https://github.com/transferthosebucks-design/credit-card-defaulter-project.git
cd credit-card-defaulter-project
```

### 2) Create and activate a virtual environment (recommended)

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install flask pandas scikit-learn
```

### 4) Start the application

```bash
python app.py
```

### 5) Open in browser

```text
http://127.0.0.1:5000
```

## Model and Dataset Notes

- Dataset: UCI Credit Card dataset (`UCI_Credit_Card.csv`)
- Current model file: `model.pkl`
- You may see a scikit-learn version warning if model and runtime versions differ. The app can still run, but for best reliability, retrain/export the model using your current scikit-learn version.

## Future Improvements

- Add `requirements.txt` with pinned versions
- Improve input validation and error handling
- Add probability score output (`predict_proba`)
- Add model performance metrics in the UI
- Containerize with Docker for deployment

## Disclaimer

This project is for educational purposes and should not be used as the sole basis for real-world financial or lending decisions.
