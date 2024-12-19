import pandas as pd

# Cargar el archivo con las métricas iniciales
archivo = "data/listings_with_features.csv"  # Cambia la ruta si es necesario
data = pd.read_csv(archivo)

# 1. Calcular Scores RFM
# Asignar puntajes (1-5) a Recency, Frequency y Monetary utilizando rangos
data['R_Score'] = pd.qcut(data['Recency'].rank(method='first'), 5, labels=[5, 4, 3, 2, 1])
data['F_Score'] = pd.qcut(data['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
data['M_Score'] = pd.qcut(data['Monetary'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])

# 2. Crear segmentos RFM
# Combinar los scores en un segmento único
data['RFM_Segment'] = data['R_Score'].astype(str) + data['F_Score'].astype(str) + data['M_Score'].astype(str)

# Crear un puntaje total para RFM
data['RFM_Score'] = data['R_Score'].astype(int) + data['F_Score'].astype(int) + data['M_Score'].astype(int)

# 3. Guardar los resultados en un archivo
resultado = "data/rfm_analysis_results.csv"  # Cambia la ruta si es necesario
data.to_csv(resultado, index=False)

print(f"Análisis RFM completado. Resultados guardados en {resultado}")
