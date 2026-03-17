import pandas as pd
import numpy as np

np.random.seed(42)
m = 100

# --- Univariate: precio según tamaño ---
size = np.random.uniform(50, 300, m)  # Tamaño en metros cuadrados
price = 1000 * size + np.random.randint(5000, 20000, m)  # Precio con ruido

df_uni = pd.DataFrame({
    'size_sqm': size, 
    'price_uds': price
})

df_uni.to_csv('data/univariate.csv', index=False)

# --- Multivariate: precio según tamaño, habitaciones y antiguedad ---
size = np.random.randint(50, 300, m)  # Tamaño en metros cuadrados
bedrooms = np.random.randint(1, 6, m)  # Número de habitaciones
age = np.random.randint(0, 40, m)  # Antigüedad en años
price = (size * 1500) + (bedrooms * 8000) - (age * 500) + np.random.randint(5000, 20000, m)  # Precio con ruido

df_multi = pd.DataFrame({
    'size_sqm': size,
    'bedrooms': bedrooms,
    'age_years': age,
    'price_uds': price
})

df_multi.to_csv('data/multivariate.csv', index=False)

print("Data generation complete.")
print(f"Univariate dataset saved to 'data/univariate.csv' with {len(df_uni)} records.")
print(f"Multivariate dataset saved to 'data/multivariate.csv' with {len(df_multi)} records.")