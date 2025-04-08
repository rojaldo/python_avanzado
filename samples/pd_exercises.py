import pandas as pd
# open mtcars.csv
try:
    df = pd.read_csv('data/mtcars.csv')
except FileNotFoundError:
    print("No se encontró el archivo 'mtcars.csv'. Asegúrate de que está en la carpeta 'data'.")
    exit()
except pd.errors.EmptyDataError:
    print("El archivo 'mtcars.csv' está vacío.")
    exit()
except pd.errors.ParserError:
    print("Error al analizar el archivo 'mtcars.csv'. Asegúrate de que está bien formado.")
    exit()
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
    exit()
else:
    print("Archivo 'mtcars.csv' cargado correctamente.")

""""
mpg - Miles per Gallon
cyl - number of cylinders
disp - displacement, in cubic inches, which is the volume of the engine
hp - horsepower
drat - driveshaft ratio, which is how fast the driveshaft is turning compared to the engine
wt - weight
qsec - 1/4 mile time; a measure of acceleration
vs - 'V' or straight - engine shape
am - transmission; auto or manual
gear - number of forward gears
carb - number of carburetors
"""

# Media de potencia de los coches

mean_hp = df['hp'].mean()
print(f"media de potencia de los coches: {mean_hp}")

# calcula el indice peso/potencia de los coches

power_to_weight = df['wt'] / df['hp']
print(f"indice peso/potencia de los coches: {power_to_weight}")

# sacar el coche mas potente

max_hp = df['hp'].max()
max_hp_index = df['hp'].idxmax()
print(f"coche mas potente: {df['model'][max_hp_index]} con {max_hp} hp")

# el que menos eficiencia de combustible 

min_mpg = df['mpg'].min()
min_mpg_index = df['mpg'].idxmin()
print(f"coche menos eficiente: {df['model'][min_mpg_index]} con {min_mpg} mpg")

# son en promedio más potentes los coches con motores en V o en línea?

# filter data for V engines (V=0)

df_v_engines = df[df['vs'] == 0]
ds_v_hp = df_v_engines['hp'].values

# filter data for straight engines (V=1)
df_straight_engines = df[df['vs'] == 1]
ds_straight_hp = df_straight_engines['hp'].values

mean_v_hp = df_v_engines['hp'].mean()
mean_straight_hp = df_straight_engines['hp'].mean()
median_v_hp = df_v_engines['hp'].median()
median_straight_hp = df_straight_engines['hp'].median()

print(f"media de potencia de los coches V: {mean_v_hp} con mediana {median_v_hp}")
print(f"media de potencia de los coches en linea: {mean_straight_hp} con mediana {median_straight_hp}")

