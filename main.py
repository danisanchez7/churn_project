from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="API de Predicción de Churn")
modelo = joblib.load('modelo_churn.pkl')

class Cliente(BaseModel):
    tenure: int
    MonthlyCharges: float

@app.get("/")
def home():
    return {"mensaje": "API de Predicción de Churn Activa. Ve a /docs para probarla."}

@app.post("/predecir")
def predecir_churn(cliente: Cliente):
    datos = pd.DataFrame([cliente.dict()])
    prediccion = modelo.predict(datos)[0]
    probabilidad = modelo.predict_proba(datos)[0][1]
    
    return {
        "prediccion_churn": bool(prediccion),
        "probabilidad": f"{probabilidad:.2%}"
    }