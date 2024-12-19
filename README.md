# airbnb-analisis-datos
Análisis de marketing basado en datos de Airbnb

## Limpieza de Datos

- Imputación de valores faltantes en `price` y `beds` con la mediana.
- Valores faltantes en `reviews_per_month` rellenados con 0.
- Fechas en `last_review` completadas con una fecha neutra (`1900-01-01`).
- Eliminación de duplicados.
- Normalización de variables para segmentación:
  - `price_normalized`, `accommodates_normalized`, `beds_normalized`.
- Creación de variables para análisis:
  - `Recency`, `Frequency`, `Monetary`.
  - `CLV` basado en proyecciones de precio y número de reseñas.
