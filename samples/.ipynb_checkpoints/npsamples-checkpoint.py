import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Crear el gráfico de líneas
plt.plot(x, y)

# Añadir etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Líneas')

# Mostrar el gráfico
plt.show()