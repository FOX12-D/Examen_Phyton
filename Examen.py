import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
data = pd.read_csv('livig.csv')

# 1. Revisión inicial del dataset
num_rows = len(data)
num_columns = len(data.columns)
avg_cost_of_living = data['Cost of living, 2017'].mean()
highest_cost_country = data.loc[data['Cost of living, 2017'].idxmax(), 'Countries']
lowest_cost_country = data.loc[data['Cost of living, 2017'].idxmin(), 'Countries']
peru_cost = data.loc[data['Countries'] == 'Peru', 'Cost of living, 2017'].values[0]
peru_rank = data.loc[data['Countries'] == 'Peru', 'Global rank'].values[0]

# Imprimir resultados
print(f"Número de filas: {num_rows}")
print(f"Número de columnas: {num_columns}")
print(f"Costo de vida promedio: {avg_cost_of_living:.2f}")
print(f"País con costo de vida más alto: {highest_cost_country}")
print(f"País con costo de vida más bajo: {lowest_cost_country}")
print(f"Costo de vida en Perú: {peru_cost}")
print(f"Ranking de Perú: {peru_rank}")

# 2. Visualizaciones

# Gráfico 1: Los 10 países con el costo de vida más alto
top_10_high = data.nlargest(10, 'Cost of living, 2017')[['Countries', 'Cost of living, 2017']]
plt.figure(figsize=(10, 6))
plt.bar(top_10_high['Countries'], top_10_high['Cost of living, 2017'], color='salmon')
plt.title('Top 10 Países con Mayor Costo de Vida (2017)')
plt.xlabel('Países')
plt.ylabel('Índice de Costo de Vida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico 2: Los 10 países con el costo de vida más bajo
top_10_low = data.nsmallest(10, 'Cost of living, 2017')[['Countries', 'Cost of living, 2017']]
plt.figure(figsize=(10, 6))
plt.bar(top_10_low['Countries'], top_10_low['Cost of living, 2017'], color='lightblue')
plt.title('Top 10 Países con Menor Costo de Vida (2017)')
plt.xlabel('Países')
plt.ylabel('Índice de Costo de Vida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico 3: Costo de vida de los países de América
america_data = data[data['Continent'] == 'America'][['Countries', 'Cost of living, 2017']]
plt.figure(figsize=(12, 6))
plt.bar(america_data['Countries'], america_data['Cost of living, 2017'], color='lightgreen')
plt.title('Costo de Vida en Países de América (2017)')
plt.xlabel('Países')
plt.ylabel('Índice de Costo de Vida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()