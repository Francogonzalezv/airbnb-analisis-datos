import pandas as pd
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler

# Cargar el archivo original filtrado
archivo = "data/listings_filtered.csv"
data = pd.read_csv(archivo)

# 1. Manejo de Valores Faltantes
# Imputar valores faltantes en 'price' y 'beds' con la mediana
data['price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)
data['price'].fillna(data['price'].median(), inplace=True)
data['beds'].fillna(data['beds'].median(), inplace=True)

# Imputar valores faltantes en 'reviews_per_month' con 0
data['reviews_per_month'].fillna(0, inplace=True)

# Convertir 'last_review' a formato de fecha, llenando valores faltantes con una fecha neutra
data['last_review'] = pd.to_datetime(data['last_review'], errors='coerce')
data['last_review'].fillna(pd.Timestamp('1900-01-01'), inplace=True)

# 2. Eliminación de duplicados
data.drop_duplicates(inplace=True)

# 3. Ajuste de Formato
# Los formatos de 'price' y 'last_review' ya fueron corregidos

# 4. Creación de Variables RFM
# Recency: Días desde la última reseña hasta hoy
hoy = datetime.now()
data['Recency'] = (hoy - data['last_review']).dt.days

# Frequency: Usamos 'number_of_reviews' como la frecuencia de reseñas
data['Frequency'] = data['number_of_reviews']

# Monetary: Basado en el precio
data['Monetary'] = data['price']

# 5. Customer Lifetime Value (CLV)
# Proyección: Número de reseñas x precio promedio
data['CLV'] = data['number_of_reviews'] * data['price']

# 6. Normalización de variables para segmentación
scaler = MinMaxScaler()
data[['price_normalized', 'accommodates_normalized', 'beds_normalized']] = scaler.fit_transform(
    data[['price', 'accommodates', 'beds']])

# Guardar el archivo procesado
data.to_csv("data/listings_with_features.csv", index=False)
