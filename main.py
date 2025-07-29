import warnings
warnings.filterwarnings("ignore")

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import pickle
import os

df = pd.read_csv("mock_churn_dataset.csv")
le = LabelEncoder()
df["ContractType"] = le.fit_transform(df["ContractType"])


with open("customer_churn.pkl", "rb") as f:
    loaded_model = pickle.load(f)


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Tenure: int = Form(...),
    MonthlyCharges: float = Form(...),
    ContractType: str = Form(...),
    UsageMetrics: float = Form(...),
    SupportTickets: int = Form(...)
):
    try:
        Tenure_MonthlyCharges = Tenure * MonthlyCharges
        Log_Usage = np.log1p(UsageMetrics)
        ContractType_Encode = le.transform([ContractType])[0]
        sample_input = [Tenure, MonthlyCharges, ContractType_Encode,
                        UsageMetrics, SupportTickets,
                        Tenure_MonthlyCharges, Log_Usage]

        predictions = loaded_model.predict([sample_input])
        if predictions[0] == 0:
            result = "No"
        else:
            result = "Yes"
    except Exception as e:
        result = f"Error: {str(e)}"

    return templates.TemplateResponse("form.html", {
        "request": request,
        "result": result
    })
