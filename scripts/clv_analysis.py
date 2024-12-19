import pandas as pd

# Cargar el archivo CSV
data = pd.read_csv('../data/rfm_analysis_results_fixed.csv')

# Calcular las métricas base
data['Avg_Value'] = data['monetary'] / data['frequency']
data['Lifetime'] = data['recency'] + data['frequency']

# Calcular CLV
data['CLV'] = data['Avg_Value'] * data['frequency'] * data['Lifetime']

# Segmentar clientes por CLV
clv_quantiles = data['CLV'].quantile([0.25, 0.5, 0.75]).to_dict()

def clv_segment(value):
    if value <= clv_quantiles[0.25]:
        return 'Low Value'
    elif value <= clv_quantiles[0.5]:
        return 'Mid Value'
    elif value <= clv_quantiles[0.75]:
        return 'High Value'
    else:
        return 'Top Value'

data['CLV_Segment'] = data['CLV'].apply(clv_segment)

# Guardar los resultados
data.to_csv('../data/airbnb_clv_analysis.csv', index=False)

# Análisis de los patrones por segmento
clv_analysis = data.groupby('CLV_Segment')[['CLV', 'Avg_Value', 'frequency', 'Lifetime']].mean()
print(clv_analysis)
