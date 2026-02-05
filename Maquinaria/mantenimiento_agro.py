import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def ejecutar_mantenimiento_predictivo():
    """Entrenamiento de modelo Random Forest y generación de alertas de riesgo."""
    
    file_path = 'sensores_maquinaria.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: No se encuentra el archivo {file_path}.")
        return

    # Carga de datos
    df = pd.read_csv(file_path)

    # Selección de variables y target
    X = df[['Horas_Uso', 'Temperatura_Motor', 'Presion_Aceite', 'Vibracion', 'Antiguedad_Anios']]
    y = df['Falla']

    # División del dataset (80% entrenamiento, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Configuración y entrenamiento del modelo Random Forest
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # Evaluación técnica del modelo
    print("Métricas de rendimiento del modelo:")
    y_pred = modelo.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Identificación de maquinaria en riesgo
    df['Prediccion_Falla'] = modelo.predict(X)
    alertas = df[df['Prediccion_Falla'] == 1]

    # Gestión de exportación
    if not os.path.exists('Resultados'):
        os.makedirs('Resultados')

    ruta_salida = 'Resultados/Maquinas_En_Riesgo.xlsx'
    alertas.to_excel(ruta_salida, index=False)
    
    print(f"Reporte de mantenimiento preventivo generado en: {ruta_salida}")

if __name__ == "__main__":
    ejecutar_mantenimiento_predictivo()