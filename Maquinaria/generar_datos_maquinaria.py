import pandas as pd
import numpy as np
from datetime import datetime

def generar_dataset(filename='sensores_maquinaria.csv'):
    """Generación de datos sintéticos de sensores para maquinaria agrícola."""
    
    np.random.seed(42)
    n_registros = 1000

    data = {
        'ID_Maquina': [f'MAQ-{i:04d}' for i in range(1, n_registros + 1)],
        'Tipo': np.random.choice(['Tractor', 'Cosechadora'], n_registros),
        'Horas_Uso': np.random.randint(100, 8000, n_registros),
        'Temperatura_Motor': np.random.uniform(60, 120, n_registros),
        'Presion_Aceite': np.random.uniform(15, 85, n_registros),
        'Vibracion': np.random.uniform(1, 15, n_registros),
        'Antiguedad_Anios': np.random.randint(1, 20, n_registros)
    }

    df = pd.DataFrame(data)

    # Lógica de falla basada en umbrales técnicos de sensores
    condicion_falla = (
        (df['Temperatura_Motor'] > 105) | 
        (df['Presion_Aceite'] < 25) | 
        (df['Vibracion'] > 12)
    )

    df['Falla'] = condicion_falla.astype(int)
    
    # Exportación a CSV en el directorio raíz
    df.to_csv(filename, index=False)
    print(f"Archivo '{filename}' generado con {n_registros} registros.")

if __name__ == "__main__":
    generar_dataset()