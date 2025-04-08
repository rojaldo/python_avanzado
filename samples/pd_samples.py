import pandas as pd

import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Nombre': ['Ana', 'Luis', 'María', 'Ana', 'Luis'], 'Edad': [27, 25, 22, 23, 30], 'Ciudad': ['Madrid', 'Lugo', 'Sevilla', 'Madrid', 'Barcelona']}

df = pd.DataFrame(data)

# Ordenar primero por 'Ciudad' y luego por 'Edad' en cada ciudad
df_multi_orden = df.sort_values(['Ciudad', 'Edad'])
print(df_multi_orden)