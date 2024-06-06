import joblib
import os

# Simulación de despliegue (por ejemplo, copiar a una carpeta de despliegue)
os.makedirs('deploy', exist_ok=True)
joblib.dump(joblib.load('model.joblib'), 'deploy/model.joblib')

print("Modelo desplegado exitosamente.")
