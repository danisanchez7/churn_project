import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Churn Predictor - Artefact Demo")

st.title("Sistema de Retención de Clientes")
st.markdown("""
Esta herramienta utiliza Inteligencia Artificial para predecir si un cliente abandonará el servicio.
**Objetivo de Negocio:** Priorizar llamadas de fidelización.
""")

st.sidebar.header("Datos del Cliente")

# Entradas del usuario
tenure = st.sidebar.slider("Antigüedad (Meses)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Cargo Mensual ($)", min_value=0.0, value=50.0)

if st.sidebar.button("Predecir Riesgo"):
    # Llamada a tu API de FastAPI (asegúrate de que esté corriendo)
    url = "http://localhost:8000/predecir"
    payload = {"tenure": tenure, "MonthlyCharges": monthly_charges}
    
    try:
        response = requests.post(url, json=payload)
        data = response.json()
        
        prob = float(data['probabilidad'].strip('%')) / 100
        
        st.subheader("Resultado de la Predicción")
        if data['prediccion_churn']:
            st.error(f" ALTO RIESGO DE ABANDONO")
        else:
            st.success(f" CLIENTE FIEL")
            
        st.metric("Probabilidad de Churn", data['probabilidad'])
        st.progress(prob)
        
    except Exception as e:
        st.error("Error: ¿Tu API está encendida? Corre 'uvicorn main:app' primero.")