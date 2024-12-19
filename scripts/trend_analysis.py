import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo de datos
data = pd.read_csv('../data/airbnb_clv_analysis.csv')

# Asegurarse de que la columna de fechas esté en formato datetime
if 'last_review' in data.columns:
    data['last_review'] = pd.to_datetime(data['last_review'])

# Patrones temporales
data['year_month'] = data['last_review'].dt.to_period('M')
temporal_patterns = data.groupby('year_month')['monetary'].sum()

# Estacionalidad
data['month'] = data['last_review'].dt.month
seasonality = data.groupby('month')['monetary'].mean()

# Tendencias a largo plazo
data = data.sort_values('last_review')
data['cumulative_monetary'] = data['monetary'].cumsum()

# Correlaciones
correlations = data[['monetary', 'frequency', 'recency', 'CLV']].corr()
print("Correlaciones entre métricas:\n", correlations)

# Guardar los resultados actualizados
data.to_csv('../data/airbnb_trend_analysis.csv', index=False)

# Visualizaciones (Opcional)
plt.figure(figsize=(10, 6))
temporal_patterns.plot(kind='line', title='Patrones Temporales de Valor Monetario', ylabel='Valor Monetario', xlabel='Tiempo (Año-Mes)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=seasonality.index, y=seasonality.values)
plt.title('Estacionalidad: Valor Monetario Promedio por Mes')
plt.xlabel('Mes')
plt.ylabel('Promedio de Valor Monetario')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(data['last_review'], data['cumulative_monetary'])
plt.title('Tendencias a Largo Plazo')
plt.xlabel('Fecha')
plt.ylabel('Valor Monetario Acumulativo')
plt.grid(True)
plt.show()
