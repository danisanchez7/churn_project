import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import kagglehub
import os
import glob

print("Descargando dataset desde Kaggle...")
path = kagglehub.dataset_download("blastchar/telco-customer-churn")

csv_files = glob.glob(os.path.join(path, "*.csv"))
if not csv_files:
    raise FileNotFoundError("No se encontró ningún archivo CSV.")

dataset_path = csv_files[0]
print(f"Cargando archivo: {dataset_path}")

df = pd.read_csv(dataset_path)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

X = df[['tenure', 'MonthlyCharges']].fillna(0) 
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

joblib.dump(modelo, 'modelo_churn.pkl')
print("¡Modelo guardado con éxito!")