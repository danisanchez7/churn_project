#  Sistema End-to-End de Predicción de Churn

Este proyecto implementa una solución completa de Machine Learning para predecir el abandono de clientes (Churn). Cubre toda la cadena de valor del dato: desde la ingesta automatizada hasta el despliegue en microservicios.

## Arquitectura del Proyecto
1. **Ingesta**: Automatizada desde Kaggle usando `kagglehub`.
2. **Procesamiento y ML**: Limpieza de datos y entrenamiento de un modelo *Random Forest* con `Scikit-Learn`.
3. **Backend**: API REST construida con `FastAPI` para servir predicciones en tiempo real.
4. **Frontend**: Interfaz interactiva con `Streamlit` para usuarios de negocio.
5. **Contenerización**: Empaquetado completo con `Docker`.

## Tecnologías
* **Lenguaje:** Python 3.10+
* **ML:** Scikit-Learn, Pandas, Joblib.
* **API:** FastAPI, Uvicorn.
* **Frontend:** Streamlit.
* **DevOps:** Docker.

## Instalación y Uso Locals

1. **Clonar el repositorio:**
   ```bash
   git clone <tu-url-de-github>
   cd churn_project

