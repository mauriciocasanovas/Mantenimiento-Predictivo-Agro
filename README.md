SISTEMA DE MANTENIMIENTO PREDICTIVO - SECTOR AGRO (MODELO IA)

DESCRIPCIÓN:
Desarrollo de una solucion de Inteligencia Artificial para el sector de maquinaria 
agricola. El sistema implementa modelos de aprendizaje supervisado para predecir 
fallas criticas en tractores y cosechadoras, permitiendo optimizar los ciclos de 
mantenimiento preventivo y reducir el tiempo de inactividad en cosecha.

ESTRUCTURA DEL PROYECTO:

1. generar_datos_maquinaria.py (Ingenieria de Datos):
   Script encargado de simular el ecosistema de telemetria. Genera un dataset de 
   1000 registros con variables de sensores (temperatura, presion y vibracion).

2. mantenimiento_agro.py (Motor de Machine Learning):
   Script principal que ejecuta el pipeline de Inteligencia Artificial:
   - Pre-procesamiento y seleccion de variables criticas (Features).
   - Entrenamiento de modelo Random Forest (Bosque Aleatorio).
   - Evaluacion de precision mediante reportes de clasificacion.
   - Generacion automatica del reporte de alertas en la carpeta /Resultados.

3. sensores_maquinaria.csv (Dataset de Entrada):
   Archivo generado por el simulador que contiene los datos crudos de los 
   sensores para ser procesados por el modelo de IA.

4. Reporte_Agro.pbix (Dashboard):
   Panel interactivo en Power BI que consume los resultados de la IA para el 
   monitoreo de flota, analisis de dispersion de fallas y deteccion de anomalias.

5. Carpeta Resultados:
   - Maquinas_En_Riesgo.xlsx: Reporte final exportado por el modelo con el 
     listado de unidades que requieren intervencion tecnica inmediata.

TECNOLOGIAS UTILIZADAS:
- Python 3.x (Lenguaje principal)
- Scikit-Learn (Random Forest para clasificacion predictiva)
- Pandas (Gestion y estructuracion de grandes volumenes de datos)
- Power BI Desktop (Visualizacion de indicadores de riesgo)

VALOR AGREGADO:
- Implementacion End-to-End: Desde la captura del dato del sensor hasta la 
  generacion de un entregable directo para el equipo tecnico.
- Modelo Predictivo Robusto: Capacidad de identificar patrones de falla no 
  evidentes mediante analisis de multiples variables simultaneas.
- Enfoque en Eficiencia Operativa: Orientado a la reduccion de costos por 
  paradas imprevistas en periodos criticos de produccion.
